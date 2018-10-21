#![allow(non_snake_case, unused_macros, unused_imports)]

// Input
macro_rules! input { (source = $s:expr, $($r:tt)*) => { let mut iter = $s.split_whitespace(); let mut next = || { iter.next().unwrap() }; input_inner!{next, $($r)*} }; ($($r:tt)*) => { let stdin = std::io::stdin(); let mut bytes = std::io::Read::bytes(std::io::BufReader::new(stdin.lock())); let mut next = move || -> String{ bytes.by_ref().map(|r|r.unwrap() as char).skip_while(|c|c.is_whitespace()).take_while(|c|!c.is_whitespace()).collect() }; input_inner!{next, $($r)*} }; }
macro_rules! input_inner { ($next:expr) => {}; ($next:expr, ) => {}; ($next:expr, $var:ident : $t:tt $($r:tt)*) => { let $var = read_value!($next, $t); input_inner!{$next $($r)*} };}
macro_rules! read_value { ($next:expr, ( $($t:tt),* )) => { ( $(read_value!($next, $t)),* ) }; ($next:expr, [ $t:tt ; $len:expr ]) => { (0..$len).map(|_| read_value!($next, $t)).collect::<Vec<_>>() }; ($next:expr, chars) => { read_value!($next, String).chars().collect::<Vec<char>>() }; ($next:expr, bytes) => { read_value!($next, String).into_bytes() }; ($next:expr, usize1) => { read_value!($next, usize) - 1 }; ($next:expr, $t:ty) => { $next().parse::<$t>().expect("Parse error") }; }

// Module
use std::cmp::{min,max};
use std::collections::{HashSet,BTreeMap};
use std::collections::VecDeque;

// Main
fn main(){
    input!{
        H: usize,
        W: usize,
        X: i64,
        S: [chars; H],
    }
    let mut S = S;
    // スタート位置、ゴール位置、答え
    let mut start = (0,0);
    let mut goal = (0,0);
    let mut ans = -1;
    // deque : 一番近いイノシシまでの距離,h,w
    let mut dq = VecDeque::new();
    // イノシシの初期位置、スタート位置、ゴール位置を記録
    for h in 0..H{
        for w in 0..W{
            if S[h][w]=='@'{
                dq.push_back((0,h,w));
            }else if S[h][w]=='S'{
                start = (h,w);
            }else if S[h][w]=='G'{
                goal = (h,w);
            }
        }
    }
    // 移動パターン
    let dhdw = [(1,0),(-1,0),(0,1),(0,-1)];
    // イノシシからの距離が近いマスを壁扱いとする
    while let Some((d,h,w)) = dq.pop_front(){
        // 壁ならスキップ
        if S[h][w]=='#'{
            continue;
        }
        // イノシシからの距離が許容できる範囲ならスキップ
        if d > X{
            continue;
        }
        // 上記条件を満たさない場合、イノシシからの距離が近いため、壁扱いとする
        S[h][w] = '#';
        // 上下左右に移動可能ならdequeに入れる
        for &(dh,dw) in dhdw.iter(){
            let th = h as i64 + dh;
            let tw = w as i64 + dw;
            // 範囲に収まっていれば
            if th>=0 && th<H as i64 && tw>=0 && tw<W as i64 {
                dq.push_back((d+1, th as usize, tw as usize));
            }
        }
    }
    // 準備完了、あとは普通に迷路をDFSで解くだけ
    let mut dq2 = VecDeque::new();
    dq2.push_back((0, start.0, start.1));
    while let Some((d,h,w)) = dq2.pop_front(){
        // 壁ならスキップ
        if S[h][w] == '#'{
            continue;
        }
        // ゴールなら出力して終了
        if (h,w) == goal{
            ans = d;
            break;
        }
        // 通過した場所は再評価しないように壁にしておく
        S[h][w] = '#';
        // 上下左右に移動可能ならdequeに入れる
        for &(dh,dw) in dhdw.iter(){
            let th = h as i64 + dh;
            let tw = w as i64 + dw;
            // 範囲に収まっていれば
            if th>=0 && th<H as i64 && tw>=0 && tw<W as i64 {
                dq2.push_back((d+1, th as usize, tw as usize));
            }
        }
    }
    // ゴール不可能なら -1 を出力
    println!("{}", ans);
}


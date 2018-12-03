#![allow(non_snake_case, unused_macros, unused_imports)]

// Input
macro_rules! input { (source = $s:expr, $($r:tt)*) => { let mut iter = $s.split_whitespace(); let mut next = || { iter.next().unwrap() }; input_inner!{next, $($r)*} }; ($($r:tt)*) => { let stdin = std::io::stdin(); let mut bytes = std::io::Read::bytes(std::io::BufReader::new(stdin.lock())); let mut next = move || -> String{ bytes.by_ref().map(|r|r.unwrap() as char).skip_while(|c|c.is_whitespace()).take_while(|c|!c.is_whitespace()).collect() }; input_inner!{next, $($r)*} }; }
macro_rules! input_inner { ($next:expr) => {}; ($next:expr, ) => {}; ($next:expr, $var:ident : $t:tt $($r:tt)*) => { let $var = read_value!($next, $t); input_inner!{$next $($r)*} };}
macro_rules! read_value { ($next:expr, ( $($t:tt),* )) => { ( $(read_value!($next, $t)),* ) }; ($next:expr, [ $t:tt ; $len:expr ]) => { (0..$len).map(|_| read_value!($next, $t)).collect::<Vec<_>>() }; ($next:expr, chars) => { read_value!($next, String).chars().collect::<Vec<char>>() }; ($next:expr, bytes) => { read_value!($next, String).into_bytes() }; ($next:expr, usize1) => { read_value!($next, usize) - 1 }; ($next:expr, $t:ty) => { $next().parse::<$t>().expect("Parse error") }; }

// Module
use std::cmp::{min,max};
use std::collections::{HashSet,BTreeMap};

// Main
fn main(){
    input!{
        n: usize,
        xy: [(i64,i64); n],
    }
    let mut xy = xy;
    // パリティのチェック
    let mut even = 0;
    let mut odd = 0;
    for i in 0..n{
        if (xy[i].0 + xy[i].1)%2==0{
            even += 1;
        }else{
            odd += 1;
        }
    }
    // パリティが0,1混在の場合は実現不可能
    if even>0 && odd>0 {
        println!("{}", -1);
        return;
    }
    // パリティが0の場合 → X座標を-1することでパリティが1の場合に帰着、後で調整必要
    if even>0 {
        for i in 0..n{
            xy[i].0 -= 1;
        }
    }
    // アームを準備
    let mut arms = vec![];
    for i in 0..35 {
        arms.push(2_i64.pow(i));
    }
    arms.sort_by(|a,b| b.cmp(a));
    // 順番に処理
    let mut Ans: Vec<Vec<char>> = vec![];
    for i in 0..n {
        let mut ans: Vec<char> = vec![];
        let (mut x, mut y) = (xy[i].0, xy[i].1);
        let (mut x0, mut y0) = (0,0);
        for arm in &arms {
            let tx = x - x0;
            let ty = y - y0;
            if &ty < &tx && &ty > &-tx {
                ans.push('R');
                x0 += *arm;
            }else if &ty<&tx && &ty<&-tx {
                ans.push('D');
                y0 -= *arm;
            }else if &ty>&tx && &ty<&-tx{
                ans.push('L');
                x0 -= *arm;
            }else{
                ans.push('U');
                y0 += *arm;
            }
        }
        Ans.push(ans);
    }
    // パリティが0の場合、長さ1のアームを追加して、操作の最後にRを追加
    if even>0 {
        arms.push(1);
        println!("{}", arms.len());
        for arm in arms {
            print!("{} ", arm);
        }
        println!();
        for ans in Ans {
            for c in ans {
                print!("{}", c);
            }
            println!("{}", 'R');
        }
    }else{
        println!("{}", arms.len());
        for arm in arms {
            print!("{} ", arm);
        }
        println!();
        for ans in Ans {
            for c in ans {
                print!("{}", c);
            }
            println!();
        }
    }
}



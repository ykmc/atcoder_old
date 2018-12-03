#![allow(non_snake_case, unused_macros, unused_imports)]

// Input
macro_rules! input { (source = $s:expr, $($r:tt)*) => { let mut iter = $s.split_whitespace(); let mut next = || { iter.next().unwrap() }; input_inner!{next, $($r)*} }; ($($r:tt)*) => { let stdin = std::io::stdin(); let mut bytes = std::io::Read::bytes(std::io::BufReader::new(stdin.lock())); let mut next = move || -> String{ bytes.by_ref().map(|r|r.unwrap() as char).skip_while(|c|c.is_whitespace()).take_while(|c|!c.is_whitespace()).collect() }; input_inner!{next, $($r)*} }; }
macro_rules! input_inner { ($next:expr) => {}; ($next:expr, ) => {}; ($next:expr, $var:ident : $t:tt $($r:tt)*) => { let $var = read_value!($next, $t); input_inner!{$next $($r)*} };}
macro_rules! read_value { ($next:expr, ( $($t:tt),* )) => { ( $(read_value!($next, $t)),* ) }; ($next:expr, [ $t:tt ; $len:expr ]) => { (0..$len).map(|_| read_value!($next, $t)).collect::<Vec<_>>() }; ($next:expr, chars) => { read_value!($next, String).chars().collect::<Vec<char>>() }; ($next:expr, bytes) => { read_value!($next, String).into_bytes() }; ($next:expr, usize1) => { read_value!($next, usize) - 1 }; ($next:expr, $t:ty) => { $next().parse::<$t>().expect("Parse error") }; }

// Module
use std::cmp::{min,max};
use std::collections::{HashSet,BTreeMap,VecDeque};

// Main
fn main(){
    input!{
        N: usize,
        A: [i64; N],
    }
    // まずは累積和
    let mut lsums = vec![0; N+1];
    let mut rsums = vec![0; N+1];
    for i in 0..N{
        lsums[i+1] = lsums[i] + A[i];
    }
    for i in 0..N{
        rsums[i+1] = rsums[i] + A[N-1-i];
    }
    // 左右からの総和0の部分列の数
    let mut lcnt = vec![0;N];
    let mut rcnt = vec![0;N];
    // 左から累積和の値の出現回数を数える
    let mut lmap = BTreeMap::new();
    for i in 0..N+1{
        *lmap.entry(&lsums[i]).or_insert(0) += 1;
        if i==1{
            lcnt[0] = *lmap.get(&lsums[i]).unwrap() - 1;
        }else if i>1{
            lcnt[i-1] = lcnt[i-2] + *lmap.get(&lsums[i]).unwrap() - 1;
        }
    }
    // 右から累積和の値の出現回数を数える
    let mut rmap = BTreeMap::new();
    for i in 0..N+1{
        *rmap.entry(&rsums[i]).or_insert(0) += 1;
        if i==1{
            rcnt[0] = *rmap.get(&rsums[i]).unwrap() - 1;
        }else if i>1{
            rcnt[i-1] = rcnt[i-2] + *rmap.get(&rsums[i]).unwrap() - 1;
        }
    }
    // 左右両端を書き換えた場合の答えで初期化
    let mut ans = min(lcnt[N-2], rcnt[N-2]);
    // 書き換える位置で全探索
    for i in 1..N-1{
        ans = min(ans, lcnt[i-1]+rcnt[N-2-i]);
    }
    // 答えを出力
    println!("{}",ans);
}


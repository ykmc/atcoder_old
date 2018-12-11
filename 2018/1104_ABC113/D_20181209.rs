#![allow(non_snake_case, unused_imports)]

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
        H: usize,
        W: usize,
        K: usize,
    }

    // 左隣(あるいは右隣)にn本の縦棒があり、真横と繋がっている時の場合の数
    let j = vec![0,1,1,2,3,5,8,13];
    // 左隣(あるいは右隣)にn本の縦棒があり、真横と繋がっていない時の場合の数
    let m = vec![1,1,2,3,5,8,13,21];

    // dp[h][w] : h行目を終えた時点でwにいる場合の数
    let mut dp = vec![vec![0 as u64; W]; H+1];
    // 初期化 : 最初は左端固定
    dp[0][0] = 1;

    // dpを更新
    for h in 1..H+1{
        for w in 0..W{
            // 右に移動
            if w != 0{
                dp[h][w] += dp[h-1][w-1] * j[w] * m[W-1-w];
            }
            // 左に移動
            if w != W-1{
                dp[h][w] += dp[h-1][w+1] * m[w] * j[W-1-w];
            }
            // 真下に移動
            dp[h][w] += dp[h-1][w] * m[w] * m[W-1-w];
            // 割った余り
            dp[h][w] %= 1_000_000_007;
        }
    }

    // K番目 は0-indexedであることに注意
    println!("{}", dp[H][K-1]);
}

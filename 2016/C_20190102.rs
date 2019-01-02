#![allow(non_snake_case, unused_imports)]

// Input
macro_rules! input { (source = $s:expr, $($r:tt)*) => { let mut iter = $s.split_whitespace(); let mut next = || { iter.next().unwrap() }; input_inner!{next, $($r)*} }; ($($r:tt)*) => { let stdin = std::io::stdin(); let mut bytes = std::io::Read::bytes(std::io::BufReader::new(stdin.lock())); let mut next = move || -> String{ bytes.by_ref().map(|r|r.unwrap() as char).skip_while(|c|c.is_whitespace()).take_while(|c|!c.is_whitespace()).collect() }; input_inner!{next, $($r)*} }; }
macro_rules! input_inner { ($next:expr) => {}; ($next:expr, ) => {}; ($next:expr, $var:ident : $t:tt $($r:tt)*) => { let $var = read_value!($next, $t); input_inner!{$next $($r)*} };}
macro_rules! read_value { ($next:expr, ( $($t:tt),* )) => { ( $(read_value!($next, $t)),* ) }; ($next:expr, [ $t:tt ; $len:expr ]) => { (0..$len).map(|_| read_value!($next, $t)).collect::<Vec<_>>() }; ($next:expr, chars) => { read_value!($next, String).chars().collect::<Vec<char>>() }; ($next:expr, bytes) => { read_value!($next, String).into_bytes() }; ($next:expr, usize1) => { read_value!($next, usize) - 1 }; ($next:expr, $t:ty) => { $next().parse::<$t>().expect("Parse error") }; }

// Module
use std::cmp::{min,max};
use std::collections::{HashSet,BTreeMap,VecDeque};

// Functions

// Main
fn main(){
    input!{
        N: usize,
        A: usize,
        XX: [usize; N],
    }

    // 1枚も使わない場合を考慮するために先頭に0を追加しておく
    let mut X = vec![0;1];
    X.extend(XX);

    // dp[n][k][s] : n枚目までからk枚選んで合計をsにする場合の数
    let mut dp = vec![vec![vec![0; 2501]; N+1]; N+1];
    dp[0][0][0] = 1;

    // dpテーブルの更新
    for n in 1..N+1{
        for k in 0..n+1{
            for s in 0..50*k+1{
                // 配列外参照を防止、この場合はn枚目を使わないパターン
                if s < X[n]{
                    dp[n][k][s] = dp[n-1][k][s];
                // n枚目を使わない場合、使う場合で場合分け
                }else if s >= X[n] && k >= 1{
                    dp[n][k][s] = dp[n-1][k][s] + dp[n-1][k-1][s-X[n]];
                }
            }
        }
    }

    let mut Ans = 0 as u64;
    for i in 1..N+1{
        Ans += dp[N][i][A*i];
    }
    println!("{}",Ans);
}
#![allow(non_snake_case, unused_imports)]

// Input
macro_rules! input { (source = $s:expr, $($r:tt)*) => { let mut iter = $s.split_whitespace(); let mut next = || { iter.next().unwrap() }; input_inner!{next, $($r)*} }; ($($r:tt)*) => { let stdin = std::io::stdin(); let mut bytes = std::io::Read::bytes(std::io::BufReader::new(stdin.lock())); let mut next = move || -> String{ bytes.by_ref().map(|r|r.unwrap() as char).skip_while(|c|c.is_whitespace()).take_while(|c|!c.is_whitespace()).collect() }; input_inner!{next, $($r)*} }; }
macro_rules! input_inner { ($next:expr) => {}; ($next:expr, ) => {}; ($next:expr, $var:ident : $t:tt $($r:tt)*) => { let $var = read_value!($next, $t); input_inner!{$next $($r)*} };}
macro_rules! read_value { ($next:expr, ( $($t:tt),* )) => { ( $(read_value!($next, $t)),* ) }; ($next:expr, [ $t:tt ; $len:expr ]) => { (0..$len).map(|_| read_value!($next, $t)).collect::<Vec<_>>() }; ($next:expr, chars) => { read_value!($next, String).chars().collect::<Vec<char>>() }; ($next:expr, bytes) => { read_value!($next, String).into_bytes() }; ($next:expr, usize1) => { read_value!($next, usize) - 1 }; ($next:expr, $t:ty) => { $next().parse::<$t>().expect("Parse error") }; }

// Module
use std::cmp::{min,max};
use std::collections::{HashSet,HashMap,BTreeMap,VecDeque};

// Functions

// Main
fn main(){
    input!{
        N: usize,
        M: usize,
        A: [usize; M]
    }
    // Aを降順ソート
    let mut A = A;
    A.sort_by(|a, b| b.cmp(a));
    // 数字を表現するのに必要なマッチ本数
    let num = vec![0,2,5,5,4,5,6,3,7,6];
    // dp : i本のマッチで表現可能な最大桁数
    let mut dp = vec![None; N+1];
    // dp初期化
    dp[0] = Some(0);
    for i in 0..M{
        if num[A[i]]<=N{
            dp[num[A[i]]] = Some(1);
        }
    }
    // dp更新
    for i in 1..N+1{
        for j in 0..M{
            if i >= num[A[j]] && dp[i-num[A[j]]]!=None{
                dp[i] = max(dp[i], dp[i-num[A[j]]].map(|x| x+1));
            }
        }
    }
    // 復元
    let mut N = N;
    let mut ans = vec![0; dp[N].unwrap()];
    for i in 0..dp[N].unwrap(){
        for j in 0..M{
            if N>=num[A[j]] && dp[N-num[A[j]]]==dp[N].map(|x| x-1){
                ans[i] = A[j];
                N -= num[A[j]];
                break
            }
        }
    }
    for a in ans{
        print!("{}", a);
    }
}
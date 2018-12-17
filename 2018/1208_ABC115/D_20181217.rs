#![allow(non_snake_case, unused_imports)]

// Input
macro_rules! input { (source = $s:expr, $($r:tt)*) => { let mut iter = $s.split_whitespace(); let mut next = || { iter.next().unwrap() }; input_inner!{next, $($r)*} }; ($($r:tt)*) => { let stdin = std::io::stdin(); let mut bytes = std::io::Read::bytes(std::io::BufReader::new(stdin.lock())); let mut next = move || -> String{ bytes.by_ref().map(|r|r.unwrap() as char).skip_while(|c|c.is_whitespace()).take_while(|c|!c.is_whitespace()).collect() }; input_inner!{next, $($r)*} }; }
macro_rules! input_inner { ($next:expr) => {}; ($next:expr, ) => {}; ($next:expr, $var:ident : $t:tt $($r:tt)*) => { let $var = read_value!($next, $t); input_inner!{$next $($r)*} };}
macro_rules! read_value { ($next:expr, ( $($t:tt),* )) => { ( $(read_value!($next, $t)),* ) }; ($next:expr, [ $t:tt ; $len:expr ]) => { (0..$len).map(|_| read_value!($next, $t)).collect::<Vec<_>>() }; ($next:expr, chars) => { read_value!($next, String).chars().collect::<Vec<char>>() }; ($next:expr, bytes) => { read_value!($next, String).into_bytes() }; ($next:expr, usize1) => { read_value!($next, usize) - 1 }; ($next:expr, $t:ty) => { $next().parse::<$t>().expect("Parse error") }; }

// Module
use std::cmp::{min,max};
use std::collections::{HashSet,BTreeMap,VecDeque};

// Functions
fn dfs(n:usize, x:i64, total:Vec<i64>, patty:Vec<i64>) -> i64{
    if n==0{
        // Lv.0
        if x>0{
            return 1;
        // 対象外
        }else{
            return 0;
        }
    // 下側のLv.n-1 まで
    }else if x <= total[n-1]+1{
        return dfs(n-1, x-1, total, patty);
    // 真ん中のパティまで
    }else if x == total[n-1]+2{
        return patty[n-1] +1;
    // 上側のLv.n-1 まで
    }else{
        return patty[n-1] + 1 + dfs(n-1, x-2-total[n-1], total, patty);
    }
}

// Main
fn main(){
    input!{
        N: usize,
        X: i64,
    }
    // Lv N バーガーの層数と、バンの数を事前計算
    let mut total = vec![0; N+1];
    let mut patty = vec![0; N+1];
    total[0] = 1; patty[0] = 1;
    for i in 1..N+1{
        total[i] = total[i-1]*2 + 3; 
        patty[i] = patty[i-1]*2 + 1;
    }
    // 与えられた問題を解く
    let ans = dfs(N, X, total, patty);

    println!("{}", ans);
}

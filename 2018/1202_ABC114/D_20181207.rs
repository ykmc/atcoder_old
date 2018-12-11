#![allow(non_snake_case, unused_imports)]

// Input
macro_rules! input { (source = $s:expr, $($r:tt)*) => { let mut iter = $s.split_whitespace(); let mut next = || { iter.next().unwrap() }; input_inner!{next, $($r)*} }; ($($r:tt)*) => { let stdin = std::io::stdin(); let mut bytes = std::io::Read::bytes(std::io::BufReader::new(stdin.lock())); let mut next = move || -> String{ bytes.by_ref().map(|r|r.unwrap() as char).skip_while(|c|c.is_whitespace()).take_while(|c|!c.is_whitespace()).collect() }; input_inner!{next, $($r)*} }; }
macro_rules! input_inner { ($next:expr) => {}; ($next:expr, ) => {}; ($next:expr, $var:ident : $t:tt $($r:tt)*) => { let $var = read_value!($next, $t); input_inner!{$next $($r)*} };}
macro_rules! read_value { ($next:expr, ( $($t:tt),* )) => { ( $(read_value!($next, $t)),* ) }; ($next:expr, [ $t:tt ; $len:expr ]) => { (0..$len).map(|_| read_value!($next, $t)).collect::<Vec<_>>() }; ($next:expr, chars) => { read_value!($next, String).chars().collect::<Vec<char>>() }; ($next:expr, bytes) => { read_value!($next, String).into_bytes() }; ($next:expr, usize1) => { read_value!($next, usize) - 1 }; ($next:expr, $t:ty) => { $next().parse::<$t>().expect("Parse error") }; }

// Module
use std::cmp::{min,max};
use std::collections::{HashSet,BTreeMap,VecDeque};

// Functions
fn gets(e:&Vec<u32>, n:u32) -> u32{
    return e.iter().filter(|x| **x > n-2).collect::<Vec<&u32>>().len() as u32;
}

// Main
fn main(){
    input!{
        N: usize,
    }
    // N! を素因数分解してvecに格納
    let mut e = vec![0; 101];
    for i in 2..N+1{
        let mut p = i;
        for j in 2..N+1{
            while p%j == 0{
                e[j] += 1;
                p /= j;
            }
        }
    }
    let mut ans = 0;
    // 約数が75個になるパターンは以下の4つ
    // 1. e1^74
    ans += gets(&e,75);
    // 2. e1^24 + e2^2
    ans += gets(&e,25) * (gets(&e,3)-1);
    // 3. e1^14 + e2^4
    ans += gets(&e,15) * (gets(&e,5)-1);
    // 4. e1^4 + e2^4 + e3^2
    ans += gets(&e,5) * (gets(&e,5)-1) * (gets(&e,3)-2)/2;

    println!("{}", ans);
}

#![allow(non_snake_case, unused_imports)]

// Input
macro_rules! input { (source = $s:expr, $($r:tt)*) => { let mut iter = $s.split_whitespace(); let mut next = || { iter.next().unwrap() }; input_inner!{next, $($r)*} }; ($($r:tt)*) => { let stdin = std::io::stdin(); let mut bytes = std::io::Read::bytes(std::io::BufReader::new(stdin.lock())); let mut next = move || -> String{ bytes.by_ref().map(|r|r.unwrap() as char).skip_while(|c|c.is_whitespace()).take_while(|c|!c.is_whitespace()).collect() }; input_inner!{next, $($r)*} }; }
macro_rules! input_inner { ($next:expr) => {}; ($next:expr, ) => {}; ($next:expr, $var:ident : $t:tt $($r:tt)*) => { let $var = read_value!($next, $t); input_inner!{$next $($r)*} };}
macro_rules! read_value { ($next:expr, ( $($t:tt),* )) => { ( $(read_value!($next, $t)),* ) }; ($next:expr, [ $t:tt ; $len:expr ]) => { (0..$len).map(|_| read_value!($next, $t)).collect::<Vec<_>>() }; ($next:expr, chars) => { read_value!($next, String).chars().collect::<Vec<char>>() }; ($next:expr, bytes) => { read_value!($next, String).into_bytes() }; ($next:expr, usize1) => { read_value!($next, usize) - 1 }; ($next:expr, $t:ty) => { $next().parse::<$t>().expect("Parse error") }; }

// Module
use std::cmp::{min,max};
use std::collections::{HashSet,BTreeMap,VecDeque};

// Functions
fn init_fact(n: u64, MOD: u64) -> (Vec<u64>, Vec<u64>, Vec<u64>){
    let mut fact = vec![1; n as usize];
    let mut finv = vec![1; n as usize];
    let mut inv  = vec![1; n as usize];
    for i in 2..n as usize{
        fact[i] = (fact[i-1] * i as u64) % MOD;
        inv[i]  = MOD - inv[(MOD as usize)%i] * (MOD/(i as u64))%MOD;
        finv[i] = finv[i-1] * inv[i] % MOD;
    }
    return (fact,finv,inv);
}

fn nCr(n: u64, r: u64, MOD: u64, fact: &Vec<u64>, finv: &Vec<u64>) -> u64{
    if n<r { return 0; }
    return fact[n as usize] * (finv[r as usize] * finv[(n-r) as usize] % MOD) % MOD;
}

// Main
fn main(){
    input!{
        H: u64,
        W: u64,
        A: u64,
        B: u64,
    }
    let modulo = 1_000_000_007;
    let f = init_fact(200_000,modulo);
    let fact = f.0;
    let finv = f.1;

    let mut ans: u64 = 0;
    for i in 0..H-A{
        ans += nCr(i+B-1,i,modulo,&fact,&finv) * nCr(H-i-1+W-B-1,W-B-1,modulo,&fact,&finv);
        ans %= modulo;
    }
    println!("{}", ans);
}
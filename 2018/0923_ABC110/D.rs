#![allow(non_snake_case)]

// Input
#[allow(unused_macros)]
macro_rules! input { (source = $s:expr, $($r:tt)*) => { let mut iter = $s.split_whitespace(); let mut next = || { iter.next().unwrap() }; input_inner!{next, $($r)*} }; ($($r:tt)*) => { let stdin = std::io::stdin(); let mut bytes = std::io::Read::bytes(std::io::BufReader::new(stdin.lock())); let mut next = move || -> String{ bytes.by_ref().map(|r|r.unwrap() as char).skip_while(|c|c.is_whitespace()).take_while(|c|!c.is_whitespace()).collect() }; input_inner!{next, $($r)*} }; }
macro_rules! input_inner { ($next:expr) => {}; ($next:expr, ) => {}; ($next:expr, $var:ident : $t:tt $($r:tt)*) => { let $var = read_value!($next, $t); input_inner!{$next $($r)*} };}
macro_rules! read_value { ($next:expr, ( $($t:tt),* )) => { ( $(read_value!($next, $t)),* ) }; ($next:expr, [ $t:tt ; $len:expr ]) => { (0..$len).map(|_| read_value!($next, $t)).collect::<Vec<_>>() }; ($next:expr, chars) => { read_value!($next, String).chars().collect::<Vec<char>>() }; ($next:expr, bytes) => { read_value!($next, String).into_bytes() }; ($next:expr, usize1) => { read_value!($next, usize) - 1 }; ($next:expr, $t:ty) => { $next().parse::<$t>().expect("Parse error") }; }

// Module
#[allow(unused_imports)]
use std::cmp::{min,max};

// Main
fn main(){
    input!{
        n: u64,
        m: u64,
    }
    let root_m = (m as f64).powf(0.5).ceil() as u64;
    let p = enum_prime(root_m);
    let pf = prime_factorization(m, &p);
    let MOD = 1000000007;
    let (fact,finv,_inv) = init_fact(200000, MOD);
    let mut ans = 1;
    for (p,cnt) in pf{
        ans = ans * nHr(n,cnt,MOD,&fact,&finv) %MOD;
    }
    println!("{}",ans);
}

fn enum_prime(n: u64) -> Vec<u64>{
    let mut prime = vec![];
    let mut is_prime = vec![true; n as usize + 1];
    is_prime[0] = false;
    is_prime[1] = false;
    for i in 2..n as usize{
        if is_prime[i] == true{
            prime.push(i as u64);
            let mut j = 2;
            while (i*j) as u64 <= n{
                is_prime[i*j] = false;
                j += 1;
            }
        }
    }
    return prime;
}

fn prime_factorization(n: u64, primes: &Vec<u64>) -> Vec<(u64,u64)>{
    let mut n = n;
    let mut res = vec![];
    for p in primes{
        let p: u64 = *p;
        let mut cnt = 0;
        while n%p == 0{
            cnt += 1;
            n /= p;
        }
        if cnt > 0{
            res.push((p, cnt));
        }
    }
    if n > 1{
        res.push((n,1));
    }
    return res;
}

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

fn nHr(n: u64, r: u64, MOD: u64, fact: &Vec<u64>, finv: &Vec<u64>) -> u64{
    if n==0 && r==0{ return 1; }
    return nCr(n+r-1, r, MOD, fact, finv);
}


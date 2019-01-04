#![allow(non_snake_case, unused_imports)]

// Input
macro_rules! input { (source = $s:expr, $($r:tt)*) => { let mut iter = $s.split_whitespace(); let mut next = || { iter.next().unwrap() }; input_inner!{next, $($r)*} }; ($($r:tt)*) => { let stdin = std::io::stdin(); let mut bytes = std::io::Read::bytes(std::io::BufReader::new(stdin.lock())); let mut next = move || -> String{ bytes.by_ref().map(|r|r.unwrap() as char).skip_while(|c|c.is_whitespace()).take_while(|c|!c.is_whitespace()).collect() }; input_inner!{next, $($r)*} }; }
macro_rules! input_inner { ($next:expr) => {}; ($next:expr, ) => {}; ($next:expr, $var:ident : $t:tt $($r:tt)*) => { let $var = read_value!($next, $t); input_inner!{$next $($r)*} };}
macro_rules! read_value { ($next:expr, ( $($t:tt),* )) => { ( $(read_value!($next, $t)),* ) }; ($next:expr, [ $t:tt ; $len:expr ]) => { (0..$len).map(|_| read_value!($next, $t)).collect::<Vec<_>>() }; ($next:expr, chars) => { read_value!($next, String).chars().collect::<Vec<char>>() }; ($next:expr, bytes) => { read_value!($next, String).into_bytes() }; ($next:expr, usize1) => { read_value!($next, usize) - 1 }; ($next:expr, $t:ty) => { $next().parse::<$t>().expect("Parse error") }; }

// Module
use std::cmp::{min,max};
use std::collections::{HashSet,BTreeMap,VecDeque};

// Functions
fn f(b:i64, n:i64) -> i64{
    if n/b == 0{
        return n;
    }else{
        return n%b + f(b,n/b);
    }
}

// Main
fn main(){
    input!{
        N: i64,
        S: i64,
    }
    let mut ans = -1;
    if N==S{
        ans = N+1;
    }else{
        let limN = (N as f64).powf(0.5).ceil() as usize;
        for b in 2..limN{
            if f(b as i64,N)==S{
                ans = b as i64;
                break;
            }
        }
        if ans == -1{
            for i in 0..limN{
                let b = (N-S)/(limN-i) as i64+1;
                if b>1{
                    if f(b,N)==S{
                        ans = b;
                        break;
                    }
                }
            }
        }
    }
    println!("{}",ans);
}
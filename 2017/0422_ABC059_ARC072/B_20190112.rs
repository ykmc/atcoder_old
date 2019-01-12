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
        A: String,
        B: String,
    }
    let mut Ans = "EQUAL";
    if A.len() > B.len(){
        Ans = "GREATER";
    }else if A.len() < B.len(){
        Ans = "LESS";
    }else{
        let aa:Vec<char> = A.chars().collect();
        let bb:Vec<char> = B.chars().collect();
        let len = A.len();
        for i in 0..len{
            if aa[i] > bb[i]{
                Ans = "GREATER";
                break;
            }else if aa[i] < bb[i]{
                Ans = "LESS";
                break;
            }
        }
    }
    println!("{}",Ans);
}
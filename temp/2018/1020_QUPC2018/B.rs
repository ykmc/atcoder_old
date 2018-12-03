#![allow(non_snake_case, unused_macros, unused_imports)]

// Input
macro_rules! input { (source = $s:expr, $($r:tt)*) => { let mut iter = $s.split_whitespace(); let mut next = || { iter.next().unwrap() }; input_inner!{next, $($r)*} }; ($($r:tt)*) => { let stdin = std::io::stdin(); let mut bytes = std::io::Read::bytes(std::io::BufReader::new(stdin.lock())); let mut next = move || -> String{ bytes.by_ref().map(|r|r.unwrap() as char).skip_while(|c|c.is_whitespace()).take_while(|c|!c.is_whitespace()).collect() }; input_inner!{next, $($r)*} }; }
macro_rules! input_inner { ($next:expr) => {}; ($next:expr, ) => {}; ($next:expr, $var:ident : $t:tt $($r:tt)*) => { let $var = read_value!($next, $t); input_inner!{$next $($r)*} };}
macro_rules! read_value { ($next:expr, ( $($t:tt),* )) => { ( $(read_value!($next, $t)),* ) }; ($next:expr, [ $t:tt ; $len:expr ]) => { (0..$len).map(|_| read_value!($next, $t)).collect::<Vec<_>>() }; ($next:expr, chars) => { read_value!($next, String).chars().collect::<Vec<char>>() }; ($next:expr, bytes) => { read_value!($next, String).into_bytes() }; ($next:expr, usize1) => { read_value!($next, usize) - 1 }; ($next:expr, $t:ty) => { $next().parse::<$t>().expect("Parse error") }; }

// Module
use std::cmp::{min,max};
use std::collections::{HashSet,BTreeMap};

// Main
fn main(){
    input!{
        q: usize,
        s: [(i64,i64,i64); q],
    }
    for i in 0..q{
        let mut a = s[i].0;
        let mut b = s[i].1;
        let mut c = s[i].2;
        let mut diff = 0;

        if a%2==1{
            diff = 100;
            diff -= min(10,b)*10;
            b -= (100-diff)/10;
            if diff > c{
                println!("{}","No");
                continue;
            }else{
                c -= diff;
                diff = 0;
            }
        }
        if b%2==1{
            diff -= 10;
            if diff<0{
                diff = -1*diff;
            }
            diff -= min(diff,c);
        }
        if c%2==0 && diff==0{
            println!("{}", "Yes");
        }else{
            println!("{}","No");
        }
    }
}


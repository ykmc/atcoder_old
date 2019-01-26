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
        Deg: usize,
        Dis: u64
    }
    let DegIndex = (Deg+112)/225;
    let DegList = vec!("N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW","N");
    let W = if Dis < 15{
        0
    }else if Dis < 15*6+3{
        1
    }else if Dis < 33*6+3{
        2
    }else if Dis < 54*6+3{
        3
    }else if Dis < 79*6+3{
        4
    }else if Dis < 107*6+3{
        5
    }else if Dis < 138*6+3{
        6
    }else if Dis < 171*6+3{
        7
    }else if Dis < 207*6+3{
        8
    }else if Dis < 244*6+3{
        9
    }else if Dis < 284*6+3{
        10
    }else if Dis < 326*6+3{
        11
    }else{
        12
    };
    println!("{} {}", if W==0{"C"}else{DegList[DegIndex]}, W);
}
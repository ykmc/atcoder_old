#![allow(non_snake_case, unused_imports)]

// Input
macro_rules! input { (source = $s:expr, $($r:tt)*) => { let mut iter = $s.split_whitespace(); let mut next = || { iter.next().unwrap() }; input_inner!{next, $($r)*} }; ($($r:tt)*) => { let stdin = std::io::stdin(); let mut bytes = std::io::Read::bytes(std::io::BufReader::new(stdin.lock())); let mut next = move || -> String{ bytes.by_ref().map(|r|r.unwrap() as char).skip_while(|c|c.is_whitespace()).take_while(|c|!c.is_whitespace()).collect() }; input_inner!{next, $($r)*} }; }
macro_rules! input_inner { ($next:expr) => {}; ($next:expr, ) => {}; ($next:expr, $var:ident : $t:tt $($r:tt)*) => { let $var = read_value!($next, $t); input_inner!{$next $($r)*} }; ($next:expr, mut $var:ident : $t:tt $($r:tt)*) => { let mut $var = read_value!($next, $t); input_inner!{$next $($r)*} }; }
macro_rules! read_value { ($next:expr, ( $($t:tt),* )) => { ( $(read_value!($next, $t)),* ) }; ($next:expr, [ $t:tt ; $len:expr ]) => { (0..$len).map(|_| read_value!($next, $t)).collect::<Vec<_>>() }; ($next:expr, [ $t:tt ]) => { { let len = read_value!($next, usize); (0..len).map(|_| read_value!($next, $t)).collect::<Vec<_>>() } }; ($next:expr, chars) => { read_value!($next, String).chars().collect::<Vec<char>>() }; ($next:expr, bytes) => { read_value!($next, String).into_bytes() }; ($next:expr, usize1) => { read_value!($next, usize) - 1 }; ($next:expr, $t:ty) => { $next().parse::<$t>().expect("Parse error") }; }

// Module
use std::cmp::{min,max};
use std::collections::{HashSet,HashMap,BTreeMap,VecDeque};

// Functions
fn bisect(x: i64, v: &Vec<i64>) -> (i64, i64) {
    match v.binary_search(&x) {
        Ok(i) => (v[i], v[i]),
        Err(i) => if i == 0 {
            (v[i], v[i])
        } else if i == v.len() {
            (v[i-1], v[i-1])
        } else {
            (v[i-1], v[i])
        }
    }
}

// Main
fn main(){
    input!{
        A: usize,
        B: usize,
        Q: usize,
        mut S: [i64; A],
        mut T: [i64; B],
        X: [i64; Q]
    }
    const INF:i64 = 1<<60;
    S.push(INF);
    S.push(-INF);
    S.sort();
    T.push(INF);
    T.push(-INF);
    T.sort();

    for x in X.into_iter(){
        let (s0,s1) = bisect(x,&S);
        let (t0,t1) = bisect(x,&T);
        let mut ans = INF;
        for &(s,t) in [(s0,t0), (s0,t1), (s1,t0), (s1,t1)].into_iter(){
            ans = min(ans, min((x-s).abs(),(x-t).abs()) + (s-t).abs());
        }
        println!("{}",ans);
    }
}
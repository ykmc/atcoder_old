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
        A: chars,
        B: chars,
        C: chars,
    }
    let mut S = HashMap::new();
    S.insert('a',A);
    S.insert('b',B);
    S.insert('c',C);
    let mut cnt = HashMap::new();
    cnt.insert('a',0);
    cnt.insert('b',0);
    cnt.insert('c',0);
    let mut turn = 'a';
    while cnt[&turn] < S[&turn].len(){
        let val:usize = *cnt.get(&turn).unwrap();
        cnt.insert(turn, val+1);
        turn = S[&turn][val];
    }
    // ↓は1.16から？
    // let ans = turn.to_uppercase().to_string();
    let ans = match turn {
        'a' => 'A',
        'b' => 'B',
        'c' => 'C',
        _ => ' '
    };
    println!("{}",ans);
}
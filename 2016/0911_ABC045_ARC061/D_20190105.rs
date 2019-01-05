#![allow(non_snake_case, unused_imports)]

// Input
macro_rules! input { (source = $s:expr, $($r:tt)*) => { let mut iter = $s.split_whitespace(); let mut next = || { iter.next().unwrap() }; input_inner!{next, $($r)*} }; ($($r:tt)*) => { let stdin = std::io::stdin(); let mut bytes = std::io::Read::bytes(std::io::BufReader::new(stdin.lock())); let mut next = move || -> String{ bytes.by_ref().map(|r|r.unwrap() as char).skip_while(|c|c.is_whitespace()).take_while(|c|!c.is_whitespace()).collect() }; input_inner!{next, $($r)*} }; }
macro_rules! input_inner { ($next:expr) => {}; ($next:expr, ) => {}; ($next:expr, $var:ident : $t:tt $($r:tt)*) => { let $var = read_value!($next, $t); input_inner!{$next $($r)*} };}
macro_rules! read_value { ($next:expr, ( $($t:tt),* )) => { ( $(read_value!($next, $t)),* ) }; ($next:expr, [ $t:tt ; $len:expr ]) => { (0..$len).map(|_| read_value!($next, $t)).collect::<Vec<_>>() }; ($next:expr, chars) => { read_value!($next, String).chars().collect::<Vec<char>>() }; ($next:expr, bytes) => { read_value!($next, String).into_bytes() }; ($next:expr, usize1) => { read_value!($next, usize) - 1 }; ($next:expr, $t:ty) => { $next().parse::<$t>().expect("Parse error") }; }

// Module
use std::cmp::{min,max};
use std::collections::{HashSet,BTreeMap,VecDeque};

// Functions

// Main
fn main(){
    input!{
        H: usize,
        W: usize,
        N: usize,
        AB: [(usize, usize); N],
    }
    // それぞれの黒マスを含む3x3全てについてmapを用いて集計
    let mut map = BTreeMap::new();
    for i in 0..N{
        let (a,b) = AB[i];
        for dh in 0..3{
            for dw in 0..3{
                // if 0<a-dh && a-dh<=H-2 && 0<b-dw && b-dw<=W-2{
                if a>dh && a<=H-2+dh && b>dw && b<=W-2+dw{
                    *map.entry((a-dh,b-dw)).or_insert(0) += 1;
                }
            }
        }
    }
    // 黒をいくつ含むか、0〜9まで集計
    let mut ans = [0 as u64; 10];
    let mut total = 0;
    for m in map{
        let ((_a,_b),v) = m;
        ans[v] += 1;
        total += 1;
    }
    // 0個は、全体 - 1つでも含むものの合計
    ans[0] = (H as u64 -2)*(W as u64 -2) - total;

    for i in 0..10{
        println!("{}", ans[i]);
    }
}
#![allow(non_snake_case, unused_imports)]

// Input
macro_rules! input { (source = $s:expr, $($r:tt)*) => { let mut iter = $s.split_whitespace(); let mut next = || { iter.next().unwrap() }; input_inner!{next, $($r)*} }; ($($r:tt)*) => { let stdin = std::io::stdin(); let mut bytes = std::io::Read::bytes(std::io::BufReader::new(stdin.lock())); let mut next = move || -> String{ bytes.by_ref().map(|r|r.unwrap() as char).skip_while(|c|c.is_whitespace()).take_while(|c|!c.is_whitespace()).collect() }; input_inner!{next, $($r)*} }; }
macro_rules! input_inner { ($next:expr) => {}; ($next:expr, ) => {}; ($next:expr, $var:ident : $t:tt $($r:tt)*) => { let $var = read_value!($next, $t); input_inner!{$next $($r)*} };}
macro_rules! read_value { ($next:expr, ( $($t:tt),* )) => { ( $(read_value!($next, $t)),* ) }; ($next:expr, [ $t:tt ; $len:expr ]) => { (0..$len).map(|_| read_value!($next, $t)).collect::<Vec<_>>() }; ($next:expr, chars) => { read_value!($next, String).chars().collect::<Vec<char>>() }; ($next:expr, bytes) => { read_value!($next, String).into_bytes() }; ($next:expr, usize1) => { read_value!($next, usize) - 1 }; ($next:expr, $t:ty) => { $next().parse::<$t>().expect("Parse error") }; }

// Module
use std::cmp::{min,max};
use std::collections::{HashSet,HashMap,BTreeMap,VecDeque,BinaryHeap};

// Functions

// Main
fn main(){
    input!{
        N: usize,
        A: [i64; N*3],
    }
    let mut sum ;
    // 左側
    let mut bheap = BinaryHeap::<i64>::new();
    let mut lsum = vec![0;1];
    for i in 0..N{
        lsum[0] += A[i];
        bheap.push(-A[i]);
    }
    sum = lsum[0];
    for i in N..N*2{
        bheap.push(-A[i]);
        sum += A[i] + bheap.pop().unwrap();
        lsum.push(sum);
    }
    // 右側
    let mut bheap = BinaryHeap::<i64>::new();
    let mut rsum = vec![0;1];
    for i in 0..N{
        rsum[0] += A[N*3-1-i];
        bheap.push(A[N*3-1-i]);
    }
    sum = rsum[0];
    for i in N..N*2{
        bheap.push(A[N*3-1-i]);
        sum += A[N*3-1-i] - bheap.pop().unwrap();
        rsum.push(sum);
    }

    // 左 - 右
    let mut ans = -9999999999999999;
    for i in 0..N+1{
        ans = max(ans, lsum[i]-rsum[N-i]);
    }
    println!("{}",ans);
}
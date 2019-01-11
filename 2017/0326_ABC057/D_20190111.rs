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
        N: usize,
        A: usize,
        B: usize,
        V: [u64; N],
    }
    let mut V = V;
    V.sort();
    V.reverse();

    let mut total = 0;
    for i in 0..A{
        total += V[i];
    }
    let ans1 = (total as f64)/(A as f64);

    let mut cnt0 = 0; // ==V[0]
    let mut cnt1 = 0; // ==V[A-1]
    let mut cnt2 = 0; // > V[A-1]
    for i in 0..N{
        if V[i]==V[0]{
            cnt0 += 1;
        }
        if V[i]==V[A-1]{
            cnt1 += 1;
        }
        if V[i] > V[A-1]{
            cnt2 += 1;
        }
    }

    let mut ans2 = 1;
    // V[0]==V[A]なら、V[0]と等しい要素を選ぶ方法を全探索
    if cnt0 > A{
        ans2 = 0;
        for i in A..(min(cnt0,B)+1){
            let mut tmp = 1;
            let c = cnt0;
            let r = i;
            for j in 0..r{
                tmp *= c-j;
                tmp /= j+1;
            }
            ans2 += tmp;
        }
    // そうでなければV[A-1]の要素を選ぶ方法を考慮
    }else{
        if cnt1+cnt2>A{
            let c = cnt1;
            let r = A-cnt2;
            for i in 0..r{
                ans2 *= c-i;
                ans2 /= i+1;
            }
        }
    }
    // print
    println!("{}", ans1);
    println!("{}", ans2);
}
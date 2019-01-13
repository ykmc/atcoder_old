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
        W: u64,
        WV: [(u64,u64); N],
    }
    // 重さごとに4分類
    let mut V = vec![vec![0;0]; 4];
    let mut w0 = 0;
    for i in 0..N{
        let (w,v) = WV[i];
        if i==0{
            V[0].push(v);
            w0 = w;
        }else{
            V[(w-w0) as usize].push(v);
        }
    }
    // 重さごとに降順ソート
    for i in 0..4{
        V[i].sort();
        V[i].reverse();
    }
    // 重さごとに累積和
    let mut S = vec![vec![0;1]; 4];
    for i in 0..4{
        let mut tmp = 0;
        for v in V[i].iter(){
            tmp += *v;
            S[i].push(tmp);
        }
    }
    // 全探索
    let mut ans = 0;
    for i0 in 0..S[0].len(){
        for i1 in 0..S[1].len(){
            for i2 in 0..S[2].len(){
                for i3 in 0..S[3].len(){
                    if w0*i0 as u64 +(w0+1)*i1 as u64 +(w0+2)*i2 as u64 +(w0+3)*i3 as u64 <= W{
                        ans = max(ans, S[0][i0]+S[1][i1]+S[2][i2]+S[3][i3]);
                    }
                }
            }
        }
    }
    println!("{}",ans);
}
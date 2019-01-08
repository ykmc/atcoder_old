#![allow(non_snake_case, unused_imports)]

// Input
macro_rules! input { (source = $s:expr, $($r:tt)*) => { let mut iter = $s.split_whitespace(); let mut next = || { iter.next().unwrap() }; input_inner!{next, $($r)*} }; ($($r:tt)*) => { let stdin = std::io::stdin(); let mut bytes = std::io::Read::bytes(std::io::BufReader::new(stdin.lock())); let mut next = move || -> String{ bytes.by_ref().map(|r|r.unwrap() as char).skip_while(|c|c.is_whitespace()).take_while(|c|!c.is_whitespace()).collect() }; input_inner!{next, $($r)*} }; }
macro_rules! input_inner { ($next:expr) => {}; ($next:expr, ) => {}; ($next:expr, $var:ident : $t:tt $($r:tt)*) => { let $var = read_value!($next, $t); input_inner!{$next $($r)*} };}
macro_rules! read_value { ($next:expr, ( $($t:tt),* )) => { ( $(read_value!($next, $t)),* ) }; ($next:expr, [ $t:tt ; $len:expr ]) => { (0..$len).map(|_| read_value!($next, $t)).collect::<Vec<_>>() }; ($next:expr, chars) => { read_value!($next, String).chars().collect::<Vec<char>>() }; ($next:expr, bytes) => { read_value!($next, String).into_bytes() }; ($next:expr, usize1) => { read_value!($next, usize) - 1 }; ($next:expr, $t:ty) => { $next().parse::<$t>().expect("Parse error") }; }

// Module
use std::cmp::{min,max};
use std::collections::{HashSet,HashMap,BTreeMap,VecDeque};

// Functions
fn dfs(visited:&mut Vec<bool>, E:&Vec<Vec<usize>>, N:usize, v:usize) -> usize {
    let mut all_visited = true;
    for i in 0..N{
        if !visited[i] {
            all_visited = false;
        }
    }
    if all_visited {
        return 1;
    }
    let mut res = 0;
    for e in &E[v]{
        if ! visited[*e] {
            visited[*e] = true;
            res += dfs(visited,E,N,*e);
            visited[*e] = false;
        }
    }
    return res;
}

// Main
fn main(){
    input!{
        N: usize,
        M: usize,
        AB: [(usize,usize); M],
    }
    let mut E = vec![vec![0; 0]; N];
    for ab in AB{
        let (a,b) = ab;
        E[a-1].push(b-1);
        E[b-1].push(a-1);
    }
//    for e in E{
//        println!("{:?}",e);
//    }
    let mut visited = vec![false; N];
    visited[0] = true;
    println!("{}", dfs(&mut visited, &E, N, 0));
}
#![allow(non_snake_case, unused_imports)]

// Input
macro_rules! input { (source = $s:expr, $($r:tt)*) => { let mut iter = $s.split_whitespace(); let mut next = || { iter.next().unwrap() }; input_inner!{next, $($r)*} }; ($($r:tt)*) => { let stdin = std::io::stdin(); let mut bytes = std::io::Read::bytes(std::io::BufReader::new(stdin.lock())); let mut next = move || -> String{ bytes.by_ref().map(|r|r.unwrap() as char).skip_while(|c|c.is_whitespace()).take_while(|c|!c.is_whitespace()).collect() }; input_inner!{next, $($r)*} }; }
macro_rules! input_inner { ($next:expr) => {}; ($next:expr, ) => {}; ($next:expr, $var:ident : $t:tt $($r:tt)*) => { let $var = read_value!($next, $t); input_inner!{$next $($r)*} };}
macro_rules! read_value { ($next:expr, ( $($t:tt),* )) => { ( $(read_value!($next, $t)),* ) }; ($next:expr, [ $t:tt ; $len:expr ]) => { (0..$len).map(|_| read_value!($next, $t)).collect::<Vec<_>>() }; ($next:expr, chars) => { read_value!($next, String).chars().collect::<Vec<char>>() }; ($next:expr, bytes) => { read_value!($next, String).into_bytes() }; ($next:expr, usize1) => { read_value!($next, usize) - 1 }; ($next:expr, $t:ty) => { $next().parse::<$t>().expect("Parse error") }; }

// Module
use std::cmp::{min,max};
use std::collections::{HashSet,BTreeMap,VecDeque};

// Main
fn main(){
    input!{
        N: usize,
        M: usize,
        PY: [(usize,u64); M],
    }
    // P(県)別にVecにまとめる、その際に何番目のデータかを一緒に記録しておく
    let mut v = vec![vec![(0,0);0]; N];
    for (i, py) in PY.iter().enumerate(){
        v[py.0 -1].push((py.1,i));
    }
    // それぞれソートする
    for i in 0..N{
        v[i].sort();
    }
    // 出力用に、最初のデータ順にまとめて
    let mut ans = vec![(0,0) ;M];
    for i in 0..N{
        for j in 0..v[i].len(){
            ans[v[i][j].1] = (i+1, j+1);
        }
    }
    // 出力する
    for i in 0..M{
        println!("{:06}{:06}",ans[i].0, ans[i].1);
    }
}

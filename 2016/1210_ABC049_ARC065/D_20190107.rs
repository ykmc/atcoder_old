#![allow(non_snake_case, unused_imports)]

// Input
macro_rules! input { (source = $s:expr, $($r:tt)*) => { let mut iter = $s.split_whitespace(); let mut next = || { iter.next().unwrap() }; input_inner!{next, $($r)*} }; ($($r:tt)*) => { let stdin = std::io::stdin(); let mut bytes = std::io::Read::bytes(std::io::BufReader::new(stdin.lock())); let mut next = move || -> String{ bytes.by_ref().map(|r|r.unwrap() as char).skip_while(|c|c.is_whitespace()).take_while(|c|!c.is_whitespace()).collect() }; input_inner!{next, $($r)*} }; }
macro_rules! input_inner { ($next:expr) => {}; ($next:expr, ) => {}; ($next:expr, $var:ident : $t:tt $($r:tt)*) => { let $var = read_value!($next, $t); input_inner!{$next $($r)*} };}
macro_rules! read_value { ($next:expr, ( $($t:tt),* )) => { ( $(read_value!($next, $t)),* ) }; ($next:expr, [ $t:tt ; $len:expr ]) => { (0..$len).map(|_| read_value!($next, $t)).collect::<Vec<_>>() }; ($next:expr, chars) => { read_value!($next, String).chars().collect::<Vec<char>>() }; ($next:expr, bytes) => { read_value!($next, String).into_bytes() }; ($next:expr, usize1) => { read_value!($next, usize) - 1 }; ($next:expr, $t:ty) => { $next().parse::<$t>().expect("Parse error") }; }

// Module
use std::cmp::{min,max};
use std::collections::{HashSet,HashMap,BTreeMap,VecDeque};

// Functions
struct UnionFind {
    par: Vec<usize>,
    rank: Vec<usize>,
}

impl UnionFind {
    fn new(n:usize) -> UnionFind {
        UnionFind {
            par: (0..n+1).collect(),
            rank: vec![0; n+1],
        }
    }
    fn find(&mut self, x:usize) -> usize {
        if self.par[x] == x {
            return x;
        }else{
            let parx = self.par[x];
            self.par[x] = self.find(parx);
            return self.par[x];
        }
    }
    fn unite(&mut self, x:usize, y:usize) {
        let x = self.find(x);
        let y = self.find(y);
        if self.rank[x] < self.rank[y] {
            self.par[x] = y;
        }else{
            self.par[y] = x;
            if self.rank[x] == self.rank[y] {
                self.rank[x] += 1;
            }
        }
    }
    fn check(&mut self, x:usize, y:usize) -> bool {
        return self.find(x) == self.find(y);
    }
}

// Main
fn main(){
    input!{
        N: usize,
        K: usize,
        L: usize,
        PQ: [(usize,usize); K],
        RS: [(usize,usize); L],
    }
    // 道路
    let mut A = UnionFind::new(N);
    for i in 0..K{
        let (x,y) = PQ[i];
        A.unite(x,y);
    }
    // 鉄道
    let mut B = UnionFind::new(N);
    for i in 0..L{
        let (x,y) = RS[i];
        B.unite(x,y);
    }
    // (道路グループ,鉄道のグループ) の組を集計
    let mut map = HashMap::new();
    for i in 1..N+1{
        let ab = (A.find(i), B.find(i));
        *map.entry(ab).or_insert(0) += 1;
    }
    // 出力
    for i in 1..N+1{
        let ab = &(A.par[i],B.par[i]);
        print!("{} ", map.get(ab).unwrap());
    }
}
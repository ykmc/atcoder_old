#![allow(non_snake_case, unused_macros, unused_imports)]

// Input
macro_rules! input { (source = $s:expr, $($r:tt)*) => { let mut iter = $s.split_whitespace(); let mut next = || { iter.next().unwrap() }; input_inner!{next, $($r)*} }; ($($r:tt)*) => { let stdin = std::io::stdin(); let mut bytes = std::io::Read::bytes(std::io::BufReader::new(stdin.lock())); let mut next = move || -> String{ bytes.by_ref().map(|r|r.unwrap() as char).skip_while(|c|c.is_whitespace()).take_while(|c|!c.is_whitespace()).collect() }; input_inner!{next, $($r)*} }; }
macro_rules! input_inner { ($next:expr) => {}; ($next:expr, ) => {}; ($next:expr, $var:ident : $t:tt $($r:tt)*) => { let $var = read_value!($next, $t); input_inner!{$next $($r)*} };}
macro_rules! read_value { ($next:expr, ( $($t:tt),* )) => { ( $(read_value!($next, $t)),* ) }; ($next:expr, [ $t:tt ; $len:expr ]) => { (0..$len).map(|_| read_value!($next, $t)).collect::<Vec<_>>() }; ($next:expr, chars) => { read_value!($next, String).chars().collect::<Vec<char>>() }; ($next:expr, bytes) => { read_value!($next, String).into_bytes() }; ($next:expr, usize1) => { read_value!($next, usize) - 1 }; ($next:expr, $t:ty) => { $next().parse::<$t>().expect("Parse error") }; }

// Module
use std::cmp::{min,max};
use std::collections::{HashSet,BTreeMap};

// Main
fn main(){
    input!{
        n: usize,
        v: [i32; n],
    }
    // BTreeMapに偶奇場合分けして格納
    let mut map1 = BTreeMap::new();
    let mut map2 = BTreeMap::new();
    for i in 0..n{
        if i%2==0{
            *map1.entry(v[i]).or_insert(0) += 1;
        }else{
            *map2.entry(v[i]).or_insert(0) += 1;
        }
    }
    // k,v逆にしてVecに格納
    let mut c1:Vec<(i32,i32)> = map1.into_iter().map(|(k,v)| (v,k)).collect();
    let mut c2:Vec<(i32,i32)> = map2.into_iter().map(|(k,v)| (v,k)).collect();
    // 全要素が同一の場合のために、ダミーで-1を0回出現として追加
    c1.push((0,-1));
    c2.push((0,-1));
    // 降順ソート
    c1.sort_by(|a,b| b.cmp(a));
    c2.sort_by(|a,b| b.cmp(a));
    // 最大の要素が同一でない場合は、それ以外を変換すれば良い
    if c1[0].1!=c2[0].1{
        println!("{}", n as i32 - (c1[0].0+c2[0].0));
    // 最大の要素が同一の場合は、2番目に多い要素まで考慮しましょう
    }else{
        println!("{}", min(n as i32 - (c1[0].0+c2[1].0),n as i32 - (c1[1].0+c2[0].0)));
    }
}

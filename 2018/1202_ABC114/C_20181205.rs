#![allow(non_snake_case, unused_imports)]

// Input
macro_rules! input { (source = $s:expr, $($r:tt)*) => { let mut iter = $s.split_whitespace(); let mut next = || { iter.next().unwrap() }; input_inner!{next, $($r)*} }; ($($r:tt)*) => { let stdin = std::io::stdin(); let mut bytes = std::io::Read::bytes(std::io::BufReader::new(stdin.lock())); let mut next = move || -> String{ bytes.by_ref().map(|r|r.unwrap() as char).skip_while(|c|c.is_whitespace()).take_while(|c|!c.is_whitespace()).collect() }; input_inner!{next, $($r)*} }; }
macro_rules! input_inner { ($next:expr) => {}; ($next:expr, ) => {}; ($next:expr, $var:ident : $t:tt $($r:tt)*) => { let $var = read_value!($next, $t); input_inner!{$next $($r)*} };}
macro_rules! read_value { ($next:expr, ( $($t:tt),* )) => { ( $(read_value!($next, $t)),* ) }; ($next:expr, [ $t:tt ; $len:expr ]) => { (0..$len).map(|_| read_value!($next, $t)).collect::<Vec<_>>() }; ($next:expr, chars) => { read_value!($next, String).chars().collect::<Vec<char>>() }; ($next:expr, bytes) => { read_value!($next, String).into_bytes() }; ($next:expr, usize1) => { read_value!($next, usize) - 1 }; ($next:expr, $t:ty) => { $next().parse::<$t>().expect("Parse error") }; }

// Module
use std::cmp::{min,max};
use std::collections::{HashSet,BTreeMap,VecDeque};

// Fn (現在値, has3, has5, has7, 上限値)
fn dfs(i:u64, b3:bool, b5:bool, b7:bool, N:u64) -> u64{
    // オーバーしてたら終了
    if i > N{
        return 0;
    }
    // オーバーしていなければカウントしていく
    let mut k = 0;
    // 3,5,7全て含んでいれば +1
    if b3 && b5 && b7{
        k += 1;
    }
    // 桁を繰り上げて調べる
    k += dfs(i*10+3, true, b5, b7, N);
    k += dfs(i*10+5, b3, true, b7, N);
    k += dfs(i*10+7, b3, b5, true, N);
    // 数え上げた数字を返す
    return k;
}

// Main
fn main(){
    input!{
        N: u64
    }
    let ans = dfs(0, false, false, false, N);
    println!("{}", ans);
}

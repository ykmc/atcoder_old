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
        S: chars,
    }
    // 1桁の場合、演算を考慮しなくてよい
    if S.len() == 1{
        println!("{}",S[0]);
    // 2桁以上の場合、演算子のパターンを全列挙して実際に計算する
    }else{
        // 演算子パターンの生成
        let mut ops:Vec<String> = vec!["+".to_string()," ".to_string()];
        let mut tmp:Vec<String> = vec![]; 
        for _ in 0..S.len()-2{
            for op in ops.iter(){
                tmp.push(format!("{}{}",op, "+"));
                tmp.push(format!("{}{}",op, " "));
            }
            ops = tmp;
            tmp = vec![];
        }
        // 計算
        let mut ans:u64 = 0;
        for op in ops{
            let mut exp = S[0].to_string();
            for (i,c) in op.chars().enumerate(){
                exp = format!("{}{}{}", exp, c, S[i+1]);
            }
            // evalしたかったけど無理っぽいので自力でやる
            exp = exp.replace(" ","");
            let nums:Vec<&str> = exp.split('+').collect();
            for num in nums{
                let x:u64 = num.parse().unwrap();
                ans += x;
            }
        }
        println!("{}",ans);
    }
}
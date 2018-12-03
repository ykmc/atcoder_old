// https://qiita.com/tanakh/items/0ba42c7ca36cd29d0ac8
#[allow(unused_macros)]
macro_rules! input {
    (source = $s:expr, $($r:tt)*) => {
        let mut iter = $s.split_whitespace();
        let mut next = || { iter.next().unwrap() };
        input_inner!{next, $($r)*}
    };
    ($($r:tt)*) => {
        let stdin = std::io::stdin();
        let mut bytes = std::io::Read::bytes(std::io::BufReader::new(stdin.lock()));
        let mut next = move || -> String{
            bytes
                .by_ref()
                .map(|r|r.unwrap() as char)
                .skip_while(|c|c.is_whitespace())
                .take_while(|c|!c.is_whitespace())
                .collect()
        };
        input_inner!{next, $($r)*}
    };
}
 
#[allow(unused_macros)]
macro_rules! input_inner {
    ($next:expr) => {};
    ($next:expr, ) => {};
 
    ($next:expr, $var:ident : $t:tt $($r:tt)*) => {
        let $var = read_value!($next, $t);
        input_inner!{$next $($r)*}
    };
}
 
#[allow(unused_macros)]
macro_rules! read_value {
    ($next:expr, ( $($t:tt),* )) => {
        ( $(read_value!($next, $t)),* )
    };
 
    ($next:expr, [ $t:tt ; $len:expr ]) => {
        (0..$len).map(|_| read_value!($next, $t)).collect::<Vec<_>>()
    };
 
    ($next:expr, chars) => {
        read_value!($next, String).chars().collect::<Vec<char>>()
    };
 
    ($next:expr, bytes) => {
        read_value!($next, String).into_bytes()
    };
 
    ($next:expr, usize1) => {
        read_value!($next, usize) - 1
    };
 
    ($next:expr, $t:ty) => {
        $next().parse::<$t>().expect("Parse error")
    };
}

// -----------------------------------------------------------------------------
// main
// -----------------------------------------------------------------------------
use std::cmp::min;
fn main(){
    input!{
        d: usize,
        g: i64,
        pc: [(i64,i64); d]
    }
    let mut ans = std::i64::MAX;
    for b in (0..1 << d){
        let mut total = 0;
        let mut cnt = 0;
        // bitが1の問題セットは全部解く
        for i in 0..d as i64{
            if b&(1<<i) != 0{
                total += (i+1)*100*pc[i as usize].0 + pc[i as usize].1;
                cnt += pc[i as usize].0;
            }
        }
        // 目標点数に不足しているなら残りの問題セットで一番配点が高いものを問題数-1まで解く
        if total >= g{
            ans = min(ans,cnt);
        }else{
            let mut si = std::i64::MAX;
            for i in 0..d as i64{
                if b&(1<<i) == 0{
                    si = i;
                }
            }
            if si<std::i64::MAX{
                for _ in 0..pc[si as usize].0-1{
                    total += (si+1)*100;
                    cnt += 1;
                    if total >= g{
                        ans = min(ans,cnt);
                        break;
                    }
                }
            }
        }
    }
    println!("{}", ans);
}


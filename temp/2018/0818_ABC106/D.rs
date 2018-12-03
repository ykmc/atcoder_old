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
fn main(){
    input!{
        n: usize,
        m: usize,
        q: usize,
        lr: [[usize; 2]; m],
        pq: [[usize; 2]; q]
    }
    let mut a = vec![vec![0;n+1];n+1];
    for lr in lr{
        let (l,r) = (lr[0],lr[1]);
        a[l-1][r-1] += 1;
    }
    for l in 0..n{
        for r in 0..n{
            a[n-l-1][r] += a[n-l][r];
        }
    }
    for r in 0..n{
        for l in 0..n{
            a[l][r+1] += a[l][r];
        }
    }
    for pq in pq{
        let (p,q) = (pq[0]-1,pq[1]-1);
        println!("{}", a[p][q]);
    }
}

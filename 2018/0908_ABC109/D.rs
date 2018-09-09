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
        h: usize,
        w: usize,
        a: [[i32; w]; h]
    }
    let mut ans = vec![];
    let mut a = a;
    for i in 0..h{
        // 偶数行は右へ進み
        if i%2==0{
            for j in 0..w-1{
                if a[i][j]%2==1{
                    a[i][j+1] += 1;
                    ans.push((i,j,i,j+1));
                }
            }
            if a[i][w-1]%2==1 && i<h-1{
                a[i+1][w-1] += 1;
                ans.push((i,w-1,i+1,w-1));
            }
        //奇数行は左へ戻る
        }else{
            for j in 0..w-1{
                if a[i][w-1-j]%2==1{
                    a[i][w-1-j-1] += 1;
                    ans.push((i,w-1-j,i,w-1-j-1));
                }
            }
            if a[i][0]%2==1 && i<h-1{
                a[i+1][0] += 1;
                ans.push((i,0,i+1,0));
            }
        }
    }
    println!("{}", ans.len());
    for (a,b,c,d) in ans{
        println!("{} {} {} {}",a+1,b+1,c+1,d+1);
    }
}

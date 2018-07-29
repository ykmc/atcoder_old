macro_rules! input {
    ($t:ty) => {
        {
            let mut line = String::new();
            std::io::stdin().read_line(&mut line).unwrap();
            line.trim().parse::<$t>().unwrap()
        }
    };
    ($($t:ty),*) => {
        {
            let mut line = String::new();
            std::io::stdin().read_line(&mut line).unwrap();
            let mut iter = line.split_whitespace();
            (
                $(iter.next().unwrap().parse::<$t>().unwrap(),)*
            )
        }
    };
    ($t:ty ;) => {
        {
            let mut line = String::new();
            std::io::stdin().read_line(&mut line).unwrap();
            line.split_whitespace()
                .map(|t| t.parse::<$t>().unwrap())
                .collect::<Vec<_>>()
        }
    };
    ($t:ty ; $n:expr) => {
        (0..$n).map(|_|
            input!($t)
        ).collect::<Vec<_>>()
    };
}

fn main(){
    let (a,b,c) = input!(usize,usize,usize);
    let mut ans = 1;
    let mut x = vec![a];
    for i in vec![b,c]{
        if x.contains(&i) {
            continue;
        }else{
            ans += 1;
            x.push(i);
        }
    }
    println!("{}", ans);
}
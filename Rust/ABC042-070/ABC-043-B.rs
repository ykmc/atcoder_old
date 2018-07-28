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
    let s = input!(String);
    let mut ans = String::new();
    for c in s.chars(){
        match c {
            '0' => ans.push_str("0"),
            '1' => ans.push_str("1"),
            'B' => {ans.pop();},
            _ => {},
        }
    }
    println!("{}", ans);
}
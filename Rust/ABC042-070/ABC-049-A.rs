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
    let c = input!(String);
    let mut ans = "consonant";
    let vowels = vec!["a","i","u","e","o"];
    if vowels.contains(&c.as_str()){
        ans = "vowel";
    }
    println!("{}", ans);
}
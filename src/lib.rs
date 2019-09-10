mod utill;

extern crate serde;
extern crate serde_pickle;

use std::collections::BTreeMap;
use std::fs;
use std::f32::consts::PI;

fn main() {
    do_all();
}
#[no_mangle]
pub fn do_all(){
    //initializing stuff
    let mut map = BTreeMap::new();
    //initialize all numbers for scenario of h0 = 0
    println!("Enter v value");
    let v = utill::next_long();
    println!("Enter starting height");
    let h = utill::next_long();
    println!("Enter angle of trajectory");
    let th = utill::next_long();
    let th = th * (PI/180.0);
    //Math calculations and assigning to map
    map.insert("v".to_string(), v);
    map.insert("h".to_string(), h);
    map.insert("th".to_string(), th);
    let serialized = serde_pickle::to_vec(&map, true).unwrap();
    fs::write("info", serialized).expect("Unable to write file");
}

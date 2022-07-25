use std::fs::read_to_string;
use std::collections::HashSet;


fn main() {
    let content = read_to_string("input").unwrap();

    let mut all_coords = vec![];
    for block in content.trim().split("\n\n") {
        let mut coords = HashSet::new();
        for line in block.split('\n').skip(1) {
            if let [a, b, c] = line.split(',').collect::<Vec<&str>>()[..] {
                coords.insert((a.parse::<i32>().unwrap(),
                               b.parse::<i32>().unwrap(),
                               c.parse::<i32>().unwrap()));
            }
        }
        all_coords.push(coords);
    }

    let axes: Vec<_> = vec![(-1, 0, 0), (0, -1, 0), (0, 0, -1), (1, 0, 0), (0, 1, 0), (0, 0, 1)];
    let mut scanners = vec![(0, 0, 0)];

    let mut total = all_coords.pop().unwrap();
    while all_coords.len() > 0 {
        let mut idx = None;
        'outer: for (i, coords) in all_coords.iter().enumerate() {
            for &x in axes.iter() {
                for &y in axes.iter() {
                    if x.0*y.0 + x.1*y.1 + x.2*y.2 == 0 {
                        let z = (x.1*y.2 - x.2*y.1, x.2*y.0 - x.0*y.2, x.0*y.1 - x.1*y.0);
                        let mut coords_tf = HashSet::new();
                        for &(a, b, c) in coords.iter() {
                            coords_tf.insert((x.0*a + x.1*b + x.2*c,
                                              y.0*a + y.1*b + y.2*c,
                                              z.0*a + z.1*b + z.2*c));
                        }
                        for &(ta, tb, tc) in total.iter() {
                            for &(a, b, c) in coords_tf.iter() {
                                let dx = ta - a;
                                let dy = tb - b;
                                let dz = tc - c;
                                let mut coords_mv = HashSet::new();
                                for &(tfx, tfy, tfz) in coords_tf.iter() {
                                    coords_mv.insert((tfx + dx, tfy + dy, tfz + dz));
                                }
                                if total.intersection(&coords_mv).count() >= 12 {
                                    let mut newtotal = HashSet::new();
                                    for &point in total.union(&coords_mv) {
                                        newtotal.insert(point);
                                    }
                                    total = newtotal;
                                    scanners.push((dx, dy, dz));
                                    idx = Some(i);
                                    break 'outer;
                                }
                            }
                        }
                    }
                }
            }
        }
        if let Some(i) = idx {
            all_coords.remove(i);
        }
    }

    let mut result = 0;
    for (i, (x1, y1, z1)) in scanners.iter().enumerate() {
        for (j, (x2, y2, z2)) in scanners.iter().enumerate() {
            if i != j {
                result = result.max((x1-x2).abs() + (y1-y2).abs() + (z1-z2).abs());
            }
        }
    }
    println!("result = {result:?}");
}

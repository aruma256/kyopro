def cross(x, y)
    x[0] * y[1] - x[1] * y[0]
end
    
def main
    ps = 4.times.map { gets.split.map(&:to_i) }
    4.times do |i|
        a, b, c = ps[i], ps[(i + 1) % 4], ps[(i + 2) % 4]
        vab = [b[0] - a[0], b[1] - a[1]]
        vbc = [c[0] - b[0], c[1] - b[1]]
        if cross(vab, vbc) < 0
            puts "No"
            return
        end
    end
    puts "Yes"
end
    
main

N = gets.to_i

def main
  m = Array.new(N) { Array.new(N) }
  (1..N).each do |i|
    j = N + 1 - i
    color = i.odd? ? '#' : '.'

    (i..j).each do |x|
      (i..j).each do |y|
        m[x-1][y-1] = color
      end
    end
  end

  m.each do |row|
    puts row.join
  end
end

main

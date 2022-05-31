N, A, B = gets.chomp.split.map(&:to_i)

f = 0
S = ".#"

N.times do
  A.times do
    ff = f
    N.times do
      B.times do
        print S[ff]
      end
      ff ^= 1
    end
    puts
  end
  f ^= 1
end

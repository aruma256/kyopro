Q = gets.chomp.to_i

def main
  stack = [0] * 100
  Q.times do
    case gets.chomp.split(" ").map(&:to_i)
    in [1, x]
      stack << x
    in [2]
      puts stack.pop
    end
  end
end

main

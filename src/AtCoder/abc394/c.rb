S = gets.chomp

def main
  ans = []
  chars = S.chars

  until chars.empty?
    c = chars.shift
    
    if c == "A" && ans.last == "W"
      ans.pop
      chars.prepend("A", "C")
    else
      ans << c
    end
  end
  
  puts ans.join
end

main

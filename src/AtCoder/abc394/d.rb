S = gets.chomp

def main
  stack = []
  chars = S.chars

  until chars.empty?
    c = chars.shift
    
    case c
    in ")" if stack.last == "("
      stack.pop
    in "]" if stack.last == "["
      stack.pop
    in ">" if stack.last == "<"
      stack.pop
    else
      stack << c
    end
  end
  
  puts stack.empty? ? "Yes" : "No"
end

main

N = gets
S = gets.chomp

def main
  S.each_char.with_index do |c, i|
    if c == '1'
      puts (i.even? ? 'Takahashi' : 'Aoki')
      return
    end
  end
end

main

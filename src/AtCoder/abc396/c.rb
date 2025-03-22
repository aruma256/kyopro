N, M = gets.chomp.split(" ").map(&:to_i)
BS = gets.chomp.split(" ").map(&:to_i)
WS = gets.chomp.split(" ").map(&:to_i)

def main
  BS.sort!
  WS.sort!

  @max_scores = 0

  # 非負の黒ボールは全て取る
  @current_score = 0
  @current_black_balls = 0

  def take_black_ball
    @current_score += BS.pop
    @current_black_balls += 1
    @max_scores = [@max_scores, @current_score].max
  end

  def take_white_ball
    @current_score += WS.pop
    @current_white_balls += 1
    @max_scores = [@max_scores, @current_score].max
  end

  # 非負の黒ボールを全て取る
  while !BS.empty? && BS.last >= 0
    take_black_ball
  end

  @current_white_balls = 0

  while true
    if @current_black_balls <= @current_white_balls
      if !BS.empty?
        take_black_ball
        next
      else
        break
      end
    end

    if !WS.empty? && WS.last > 0
      take_white_ball
      next
    else
      break
    end
  end

  puts @max_scores
end

main

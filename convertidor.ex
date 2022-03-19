defmodule ExploraLogs do
  def dia(logName) do
			{:ok, filetext} = File.read(logName)
			freqIps = Regex.scan(~r/\d+?\.\d+?\.\d+?\.\d+?/, filetext) 
								|> Enum.frequencies() 
			{nVeces, ipLoc} = Map.new(freqIps, fn {key, val} -> {val, key} end) 
								|> Enum.sort() 
								|> List.last()
			IO.puts ("#{nVeces} ocasiones desde la dirección #{ipLoc} " )
  end
end



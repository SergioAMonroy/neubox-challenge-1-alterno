defmodule convertidor do
  def obtenGanador(entrada) do
			{:ok, filetext} = File.read(entrada)
            lineas = String.split(filetext, ~r/\R/)
            primeraLinea = hd(lineas)
            rondas = Integer.parse(primeraLinea)
            detalles = tl(lineas)
            numeroDeDetalles = Enum.count(detalles)

			{nVeces, ipLoc} = Map.new(freqIps, fn {key, val} -> {val, key} end) 
								|> Enum.sort() 
								|> List.last()
			IO.puts ("#{nVeces} ocasiones desde la dirección #{ipLoc} " )
  end
end



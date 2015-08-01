--
-- Alice
--

-- Alice must already be running and reading/writing to the data folder

config.alice = {}
config.alice.help = ""
config.alice.comment = ""

piepan.On('message', function(e)
	if e.Sender == nil then
        return
    end
    if string.sub(e.Message, 0, 1) == config.command_prefix then
		return
	end
	if string.sub(e.Message, 0, 1) == '@' then
		return
	end

	--
	-- NEED TO CHECK IF SOUNDBOARD IS LOADED
	--
	if string.sub(e.Message, 0, 1) == config.soundboard.sound_prefix then
		return
	end

	local file = assert(io.open("modules/alice/data/Input.txt", "w"))
	file:write(e.Message)
	file:close()

	sleep(2)

	local f = assert(io.open("modules/alice/data/Output.txt", "r"))
    local t = f:read("*all")
    f:close()

	e.Sender.Channel.Send("@" .. e.Sender.Name .. ": " .. t, false)
end)
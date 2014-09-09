def main():
	consolidations = {
					"**" : "__",
					"-"  : "+",
					"^*" : "+",
					"*"  : "_"
				}

	# if count of * is odd, the line is a unordered list replace ^*
	replacements = {
					"#" : "<h1>",
					"##" : "<h2>",
					"###" : "<h3>",
					"####" : "<h4>",
					"#####" : "<h5>",
					"######" : "<h6>",
					" __" : " <strong>",
					"__ " : "</strong> ",
					" _" : " <em>",
					"_ " : "</em> ",
					"* " : "</em> ",
					"^1." : "<ol><li>",
					""
				}

	# only supports atx-style headers
import sublime, sublime_plugin

class DisplayMathCommand(sublime_plugin.TextCommand):
    def run(self, edit):
    	# Walk through each region in the selection
        for region in self.view.sel():
        	# Only interested in empty regions, otherwise they may span multiple
            # lines, which doesn't make sense for this command.
            if region.empty():
            	# Expand the region to the full line it resides on, excluding the newline
            	line = self.view.line(region)
            	# Extract the line content
            	line_contents = self.view.substr(line)
            	# Check if the line content is empty of just space and tabs.
            	# If empty/space/tabs insert only one new line.
            	# else inser two
            	if (not line_contents or line_contents.isspace()):
            		self.view.run_command("insert_snippet",{"contents": "\\[\n\t$1\n\\]\n\n$2"})
            	else:
            		self.view.run_command("insert_snippet",{"contents": "\n\\[\n\t$1\n\\]\n$2"})
            break # Break the loop to avoid double insertion

class AlignMathCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Walk through each region in the selection
        for region in self.view.sel():
            # Only interested in empty regions, otherwise they may span multiple
            # lines, which doesn't make sense for this command.
            if region.empty():
                # Expand the region to the full line it resides on, excluding the newline
                line = self.view.line(region)
                # Extract the line content
                line_contents = self.view.substr(line)
                # Check if the line content is empty of just space and tabs.
                # If empty/space/tabs insert only one new line.
                # else inser two
                if (not line_contents or line_contents.isspace()):
                    self.view.run_command("insert_snippet",{"contents": "\\begin{align*}\n\t$1\n\\end{align}\n$2"})
                else:
                    self.view.run_command("insert_snippet",{"contents": "\n\\begin{align*}\n\t$1\n\\end{align}\n$2"})
            break # Break the loop to avoid double insertion

class InlineMathCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet",{"contents": "\\$$1\\$"})


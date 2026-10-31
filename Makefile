DIAGRAMS := images/concept-2/diagrams
PHASES   := 1 2 3 4 5
BUILD    := build
CHROME   ?= /Applications/Google Chrome.app/Contents/MacOS/Google Chrome
CHECKER  ?= ../ai-setup/site/cards/check-agent-docs.py

.PHONY: help diagrams previews refs check screenshot open clean

help:
	@echo "make diagrams    regenerate the SVG diagrams from make_concept.py"
	@echo "make previews    render the diagrams to $(BUILD)/previews/"
	@echo "make refs        render the diagrams at 1.6x to $(BUILD)/refs/ for ElevenLabs"
	@echo "make check       verify images and local links, then run the agent-docs checker"
	@echo "make screenshot  desktop and phone screenshots of blog-post.html into $(BUILD)/"
	@echo "make open        open blog-post.html in the browser"
	@echo "make clean       remove $(BUILD)/"

diagrams:
	python3 $(DIAGRAMS)/make_concept.py $(DIAGRAMS)

previews: diagrams
	@mkdir -p $(BUILD)/previews
	@for n in $(PHASES); do rsvg-convert $(DIAGRAMS)/phase-$$n.svg -o $(BUILD)/previews/phase-$$n.png; done
	@echo "wrote $(BUILD)/previews/phase-{1..5}.png"

refs: diagrams
	@mkdir -p $(BUILD)/refs
	@for n in $(PHASES); do \
	  rsvg-convert -z 1.6 $(DIAGRAMS)/phase-$$n.svg -o $(BUILD)/refs/phase-$$n.png; \
	  echo "$(BUILD)/refs/phase-$$n.png $$(stat -f %z $(BUILD)/refs/phase-$$n.png) bytes"; \
	done

# The checker comes from the local ai-setup checkout; fall back to the site.
check:
	python3 scripts/check_post.py
	@if [ -f "$(CHECKER)" ]; then python3 -I "$(CHECKER)" .; \
	else mkdir -p $(BUILD) && curl -fsSL https://ai.memention.net/cards/check-agent-docs.py -o $(BUILD)/check-agent-docs.py \
	  && python3 -I $(BUILD)/check-agent-docs.py .; fi

# Headless Chrome won't shrink below ~500px, so the phone shot renders the page in a 390px iframe.
screenshot:
	@mkdir -p $(BUILD)
	@"$(CHROME)" --headless=new --disable-gpu --hide-scrollbars --window-size=1200,2400 \
	  --screenshot=$(BUILD)/page-desktop.png "file://$(CURDIR)/blog-post.html" 2>/dev/null
	@printf '<body style="margin:0"><iframe src="file://%s/blog-post.html" style="width:390px;height:1600px;border:0"></iframe></body>' "$(CURDIR)" > $(BUILD)/phone-frame.html
	@"$(CHROME)" --headless=new --disable-gpu --hide-scrollbars --allow-file-access-from-files --window-size=390,1600 \
	  --screenshot=$(BUILD)/page-phone.png "file://$(CURDIR)/$(BUILD)/phone-frame.html" 2>/dev/null
	@echo "wrote $(BUILD)/page-desktop.png $(BUILD)/page-phone.png"

open:
	open blog-post.html

clean:
	rm -rf $(BUILD)

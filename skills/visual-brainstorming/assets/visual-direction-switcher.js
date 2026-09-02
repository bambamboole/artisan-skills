(() => {
  const data = document.querySelector("#visual-direction-switcher-data");
  const mount = document.querySelector("#visual-direction-switcher");
  if (!data || !mount) return;

  let directions;
  try {
    directions = JSON.parse(data.textContent);
  } catch {
    return;
  }
  if (!Array.isArray(directions) || directions.length < 2) return;

  const panel = document.createElement("nav");
  panel.className = "group fixed bottom-0 left-1/2 z-50 w-[min(34rem,calc(100vw-1.5rem))] -translate-x-1/2 translate-y-[calc(100%-3rem)] rounded-t-2xl border border-white/20 bg-slate-950/95 text-white shadow-2xl backdrop-blur transition-transform duration-200 ease-out hover:translate-y-0 focus-within:translate-y-0";
  panel.setAttribute("aria-label", "Visual direction switcher");

  const list = document.createElement("div");
  list.className = "border-t border-white/15 px-3 pt-3";
  const toggle = document.createElement("button");
  toggle.className = "flex h-12 w-full items-center justify-between px-4 text-left text-sm font-semibold";
  toggle.type = "button";
  toggle.setAttribute("aria-expanded", "false");
  toggle.innerHTML = '<span>Compare directions</span><span aria-hidden="true">↑</span>';
  panel.append(toggle, list);
  mount.append(panel);

  const current = new URL(window.location.href).pathname;
  directions.forEach((direction, index) => {
    const link = document.createElement("a");
    const active = new URL(direction.href, window.location.href).pathname === current;
    link.href = direction.href;
    link.className = "mb-2 flex items-center justify-between rounded-xl px-3 py-2 transition " + (active ? "bg-white text-slate-950" : "hover:bg-white/10 focus:bg-white/10");
    if (active) link.setAttribute("aria-current", "page");

    const label = document.createElement("span");
    label.className = "font-semibold";
    label.textContent = direction.label || "Direction " + (index + 1);
    link.append(label);
    if (direction.detail) {
      const detail = document.createElement("span");
      detail.className = active ? "text-xs text-slate-600" : "text-xs text-slate-300";
      detail.textContent = direction.detail;
      link.append(detail);
    }
    list.append(link);
  });

  let pinned = false;
  const setPinned = (value) => {
    pinned = value;
    panel.classList.toggle("translate-y-0", pinned);
    panel.classList.toggle("translate-y-[calc(100%-3rem)]", !pinned);
    toggle.setAttribute("aria-expanded", String(pinned));
  };
  toggle.addEventListener("click", () => {
    setPinned(!pinned);
    if (!pinned) toggle.blur();
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && pinned) {
      setPinned(false);
      toggle.blur();
    }
  });
})();

import { defineComponent, mergeProps, useSSRContext } from 'vue';
import { ssrRenderAttrs, ssrRenderComponent } from 'vue/server-renderer';
import { _ as _export_sfc, u as useThemeManager } from './server.mjs';
import '../_/nitro.mjs';
import 'node:http';
import 'node:https';
import 'node:events';
import 'node:buffer';
import 'node:fs';
import 'node:path';
import 'better-sqlite3';
import 'node:url';
import 'ipx';
import 'node:crypto';
import 'vue-router';
import '@iconify/vue';

const _sfc_main$1 = /* @__PURE__ */ defineComponent({
  __name: "PowerMap",
  __ssrInlineRender: true,
  setup(__props) {
    useThemeManager();
    return (_ctx, _push, _parent, _attrs) => {
      _push(`<div${ssrRenderAttrs(mergeProps({ class: "map-wrapper" }, _attrs))} data-v-d062de7f><div id="map" data-v-d062de7f></div><h3 data-v-d062de7f>PowerChain</h3></div>`);
    };
  }
});
const _sfc_setup$1 = _sfc_main$1.setup;
_sfc_main$1.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("components/PowerMap.vue");
  return _sfc_setup$1 ? _sfc_setup$1(props, ctx) : void 0;
};
const PowerMap = /* @__PURE__ */ Object.assign(_export_sfc(_sfc_main$1, [["__scopeId", "data-v-d062de7f"]]), { __name: "PowerMap" });
const _sfc_main = /* @__PURE__ */ defineComponent({
  __name: "index",
  __ssrInlineRender: true,
  setup(__props) {
    return (_ctx, _push, _parent, _attrs) => {
      _push(`<main${ssrRenderAttrs(_attrs)} data-v-02c5bde7>`);
      _push(ssrRenderComponent(PowerMap, { class: "odd-section" }, null, _parent));
      _push(`<button data-v-02c5bde7>Fetch</button></main>`);
    };
  }
});
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("pages/index.vue");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
const index = /* @__PURE__ */ _export_sfc(_sfc_main, [["__scopeId", "data-v-02c5bde7"]]);

export { index as default };
//# sourceMappingURL=index-CHZyPET2.mjs.map

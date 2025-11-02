import { defineComponent, ref, useSSRContext } from 'vue';
import { ssrRenderAttrs, ssrRenderAttr, ssrInterpolate } from 'vue/server-renderer';
import { _ as _export_sfc } from './server.mjs';
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

const _sfc_main = /* @__PURE__ */ defineComponent({
  __name: "complaint",
  __ssrInlineRender: true,
  setup(__props) {
    const name = ref("");
    const phone = ref("");
    const area = ref("");
    const pincode = ref("");
    const description = ref("");
    return (_ctx, _push, _parent, _attrs) => {
      _push(`<main${ssrRenderAttrs(_attrs)} data-v-8f597fcf><div class="complaint-container" data-v-8f597fcf><h2 class="title" data-v-8f597fcf>Report a Power Outage</h2><form class="complaint-form" data-v-8f597fcf><div class="form-group" data-v-8f597fcf><label for="name" data-v-8f597fcf>Full Name</label><input id="name"${ssrRenderAttr("value", name.value)} type="text" placeholder="Enter your name" required data-v-8f597fcf></div><div class="form-group" data-v-8f597fcf><label for="phone" data-v-8f597fcf>Phone Number</label><input id="phone"${ssrRenderAttr("value", phone.value)} type="tel" placeholder="Enter your phone number" required data-v-8f597fcf></div><div class="form-group" data-v-8f597fcf><label for="area" data-v-8f597fcf>Area / Locality</label><input id="area"${ssrRenderAttr("value", area.value)} type="text" placeholder="Enter your area or village name" disabled readonly data-v-8f597fcf></div><div class="form-group" data-v-8f597fcf><label for="pincode" data-v-8f597fcf>Pincode</label><input id="pincode"${ssrRenderAttr("value", pincode.value)} type="text" placeholder="e.g. 560001" disabled readonly data-v-8f597fcf></div><div class="form-group" data-v-8f597fcf><label for="description" data-v-8f597fcf>Describe the Issue</label><textarea id="description" rows="4" placeholder="Describe the power issue or duration of outage..." data-v-8f597fcf>${ssrInterpolate(description.value)}</textarea></div><div class="form-group" data-v-8f597fcf><button type="submit" class="submit-btn" data-v-8f597fcf>Submit Complaint</button></div></form></div></main>`);
    };
  }
});
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("pages/complaint.vue");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
const complaint = /* @__PURE__ */ _export_sfc(_sfc_main, [["__scopeId", "data-v-8f597fcf"]]);

export { complaint as default };
//# sourceMappingURL=complaint-CqzcLMZ9.mjs.map

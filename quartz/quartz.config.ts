import { QuartzConfig } from "quartz/cfg"

const config: QuartzConfig = {
  configuration: {
    pageTitle: "Wiki Quartz",
    enableSPA: true,
    enablePopovers: true,
  },
  plugins: {
    transformers: [],
    filters: [],
    emitters: [],
  },
}

export default config

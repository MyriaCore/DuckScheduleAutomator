# Course Sign Up System API Docs

## Navigation
- [Home](home.md)
- [SIT Scheduler API Documentation](sitsched.md)
- [Course Signup System API Documentation](signup.md)

<!-- TODO: Find a less spammy way to include the site's files -->
<!-- TODO: Add a table of contents to this -->

## Intro

Get / Post Requests don't show up during site navigation, so it can be assumed that all the information is encoded in the website and the whole thing is somehow static, or that there's some weird js stuff going on. There's a pretty large ajax script, which will be posted in its respective section.

## Site Structure

In the sources tab of inspect element, there's a folder in `top/my.stevens.edu/default/modules/custom` that contains most of what seems to be the logic.

![site structure](https://i.imgur.com/6NIwcwd.png)

The files in `misc` seem to be related to site logic, and are documented in the [misc scripts section](). <!-- TODO: add section link -->
The folders / files in `modules` are all UI related css files. `profiles/openatrium` seems to have app/logic-related files too<sup>[[Citation Needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)]</sup>. Everything in `sites` is pretty much misc. UI / authentication stuff.

![folder structure](https://i.imgur.com/44p1All.png)

All of these folders have a cooresponding `{foldername}.js` file in them. `my_stevens_feedback` has a `feedback.css` file in it, however.

`stevens_mystevens_api_badge.js` and `stevens_mystevens_detect_network.js` both seem to be for user identification / verification, implying the over-arching site logic is elsewhere. The files in `stevens_mystevens_feedback` and `stevens_mystevens_flexslider_link` seem to be UI/UX related.

<!-- TODO: document the rest of the site structure -->


## HTML
This is the single html file in the whole thing.
```html
<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" version="XHTML+RDFa 1.0" dir="ltr">
    <head profile="http://www.w3.org/1999/xhtml/vocab">
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
        <script type="text/javascript">
            (window.NREUM || (NREUM = {})).loader_config = {
                xpid: "Vw8FU1VSGwYCVlRTDwM="
            };
            window.NREUM || (NREUM = {}),
            __nr_require = function(t, n, e) {
                function r(e) {
                    if (!n[e]) {
                        var o = n[e] = {
                            exports: {}
                        };
                        t[e][0].call(o.exports, function(n) {
                            var o = t[e][1][n];
                            return r(o || n)
                        }, o, o.exports)
                    }
                    return n[e].exports
                }
                if ("function" == typeof __nr_require)
                    return __nr_require;
                for (var o = 0; o < e.length; o++)
                    r(e[o]);
                return r
            }({
                1: [function(t, n, e) {
                    function r(t) {
                        try {
                            s.console && console.log(t)
                        } catch (n) {}
                    }
                    var o, i = t("ee"), a = t(16), s = {};
                    try {
                        o = localStorage.getItem("__nr_flags").split(","),
                        console && "function" == typeof console.log && (s.console = !0,
                        o.indexOf("dev") !== -1 && (s.dev = !0),
                        o.indexOf("nr_dev") !== -1 && (s.nrDev = !0))
                    } catch (c) {}
                    s.nrDev && i.on("internal-error", function(t) {
                        r(t.stack)
                    }),
                    s.dev && i.on("fn-err", function(t, n, e) {
                        r(e.stack)
                    }),
                    s.dev && (r("NR AGENT IN DEVELOPMENT MODE"),
                    r("flags: " + a(s, function(t, n) {
                        return t
                    }).join(", ")))
                }
                , {}],
                2: [function(t, n, e) {
                    function r(t, n, e, r, s) {
                        try {
                            p ? p -= 1 : o(s || new UncaughtException(t,n,e), !0)
                        } catch (f) {
                            try {
                                i("ierr", [f, c.now(), !0])
                            } catch (d) {}
                        }
                        return "function" == typeof u && u.apply(this, a(arguments))
                    }
                    function UncaughtException(t, n, e) {
                        this.message = t || "Uncaught error with no additional information",
                        this.sourceURL = n,
                        this.line = e
                    }
                    function o(t, n) {
                        var e = n ? null : c.now();
                        i("err", [t, e])
                    }
                    var i = t("handle")
                      , a = t(17)
                      , s = t("ee")
                      , c = t("loader")
                      , f = t("gos")
                      , u = window.onerror
                      , d = !1
                      , l = "nr@seenError"
                      , p = 0;
                    c.features.err = !0,
                    t(1),
                    window.onerror = r;
                    try {
                        throw new Error
                    } catch (h) {
                        "stack"in h && (t(8),
                        t(7),
                        "addEventListener"in window && t(5),
                        c.xhrWrappable && t(9),
                        d = !0)
                    }
                    s.on("fn-start", function(t, n, e) {
                        d && (p += 1)
                    }),
                    s.on("fn-err", function(t, n, e) {
                        d && !e[l] && (f(e, l, function() {
                            return !0
                        }),
                        this.thrown = !0,
                        o(e))
                    }),
                    s.on("fn-end", function() {
                        d && !this.thrown && p > 0 && (p -= 1)
                    }),
                    s.on("internal-error", function(t) {
                        i("ierr", [t, c.now(), !0])
                    })
                }
                , {}],
                3: [function(t, n, e) {
                    t("loader").features.ins = !0
                }
                , {}],
                4: [function(t, n, e) {
                    function r(t) {}
                    if (window.performance && window.performance.timing && window.performance.getEntriesByType) {
                        var o = t("ee")
                          , i = t("handle")
                          , a = t(8)
                          , s = t(7)
                          , c = "learResourceTimings"
                          , f = "addEventListener"
                          , u = "resourcetimingbufferfull"
                          , d = "bstResource"
                          , l = "resource"
                          , p = "-start"
                          , h = "-end"
                          , m = "fn" + p
                          , v = "fn" + h
                          , w = "bstTimer"
                          , y = "pushState"
                          , g = t("loader");
                        g.features.stn = !0,
                        t(6);
                        var b = NREUM.o.EV;
                        o.on(m, function(t, n) {
                            var e = t[0];
                            e instanceof b && (this.bstStart = g.now())
                        }),
                        o.on(v, function(t, n) {
                            var e = t[0];
                            e instanceof b && i("bst", [e, n, this.bstStart, g.now()])
                        }),
                        a.on(m, function(t, n, e) {
                            this.bstStart = g.now(),
                            this.bstType = e
                        }),
                        a.on(v, function(t, n) {
                            i(w, [n, this.bstStart, g.now(), this.bstType])
                        }),
                        s.on(m, function() {
                            this.bstStart = g.now()
                        }),
                        s.on(v, function(t, n) {
                            i(w, [n, this.bstStart, g.now(), "requestAnimationFrame"])
                        }),
                        o.on(y + p, function(t) {
                            this.time = g.now(),
                            this.startPath = location.pathname + location.hash
                        }),
                        o.on(y + h, function(t) {
                            i("bstHist", [location.pathname + location.hash, this.startPath, this.time])
                        }),
                        f in window.performance && (window.performance["c" + c] ? window.performance[f](u, function(t) {
                            i(d, [window.performance.getEntriesByType(l)]),
                            window.performance["c" + c]()
                        }, !1) : window.performance[f]("webkit" + u, function(t) {
                            i(d, [window.performance.getEntriesByType(l)]),
                            window.performance["webkitC" + c]()
                        }, !1)),
                        document[f]("scroll", r, {
                            passive: !0
                        }),
                        document[f]("keypress", r, !1),
                        document[f]("click", r, !1)
                    }
                }
                , {}],
                5: [function(t, n, e) {
                    function r(t) {
                        for (var n = t; n && !n.hasOwnProperty(u); )
                            n = Object.getPrototypeOf(n);
                        n && o(n)
                    }
                    function o(t) {
                        s.inPlace(t, [u, d], "-", i)
                    }
                    function i(t, n) {
                        return t[1]
                    }
                    var a = t("ee").get("events")
                      , s = t(19)(a, !0)
                      , c = t("gos")
                      , f = XMLHttpRequest
                      , u = "addEventListener"
                      , d = "removeEventListener";
                    n.exports = a,
                    "getPrototypeOf"in Object ? (r(document),
                    r(window),
                    r(f.prototype)) : f.prototype.hasOwnProperty(u) && (o(window),
                    o(f.prototype)),
                    a.on(u + "-start", function(t, n) {
                        var e = t[1]
                          , r = c(e, "nr@wrapped", function() {
                            function t() {
                                if ("function" == typeof e.handleEvent)
                                    return e.handleEvent.apply(e, arguments)
                            }
                            var n = {
                                object: t,
                                "function": e
                            }[typeof e];
                            return n ? s(n, "fn-", null, n.name || "anonymous") : e
                        });
                        this.wrapped = t[1] = r
                    }),
                    a.on(d + "-start", function(t) {
                        t[1] = this.wrapped || t[1]
                    })
                }
                , {}],
                6: [function(t, n, e) {
                    var r = t("ee").get("history")
                      , o = t(19)(r);
                    n.exports = r,
                    o.inPlace(window.history, ["pushState", "replaceState"], "-")
                }
                , {}],
                7: [function(t, n, e) {
                    var r = t("ee").get("raf")
                      , o = t(19)(r)
                      , i = "equestAnimationFrame";
                    n.exports = r,
                    o.inPlace(window, ["r" + i, "mozR" + i, "webkitR" + i, "msR" + i], "raf-"),
                    r.on("raf-start", function(t) {
                        t[0] = o(t[0], "fn-")
                    })
                }
                , {}],
                8: [function(t, n, e) {
                    function r(t, n, e) {
                        t[0] = a(t[0], "fn-", null, e)
                    }
                    function o(t, n, e) {
                        this.method = e,
                        this.timerDuration = isNaN(t[1]) ? 0 : +t[1],
                        t[0] = a(t[0], "fn-", this, e)
                    }
                    var i = t("ee").get("timer")
                      , a = t(19)(i)
                      , s = "setTimeout"
                      , c = "setInterval"
                      , f = "clearTimeout"
                      , u = "-start"
                      , d = "-";
                    n.exports = i,
                    a.inPlace(window, [s, "setImmediate"], s + d),
                    a.inPlace(window, [c], c + d),
                    a.inPlace(window, [f, "clearImmediate"], f + d),
                    i.on(c + u, r),
                    i.on(s + u, o)
                }
                , {}],
                9: [function(t, n, e) {
                    function r(t, n) {
                        d.inPlace(n, ["onreadystatechange"], "fn-", s)
                    }
                    function o() {
                        var t = this
                          , n = u.context(t);
                        t.readyState > 3 && !n.resolved && (n.resolved = !0,
                        u.emit("xhr-resolved", [], t)),
                        d.inPlace(t, y, "fn-", s)
                    }
                    function i(t) {
                        g.push(t),
                        h && (x ? x.then(a) : v ? v(a) : (E = -E,
                        O.data = E))
                    }
                    function a() {
                        for (var t = 0; t < g.length; t++)
                            r([], g[t]);
                        g.length && (g = [])
                    }
                    function s(t, n) {
                        return n
                    }
                    function c(t, n) {
                        for (var e in t)
                            n[e] = t[e];
                        return n
                    }
                    t(5);
                    var f = t("ee")
                      , u = f.get("xhr")
                      , d = t(19)(u)
                      , l = NREUM.o
                      , p = l.XHR
                      , h = l.MO
                      , m = l.PR
                      , v = l.SI
                      , w = "readystatechange"
                      , y = ["onload", "onerror", "onabort", "onloadstart", "onloadend", "onprogress", "ontimeout"]
                      , g = [];
                    n.exports = u;
                    var b = window.XMLHttpRequest = function(t) {
                        var n = new p(t);
                        try {
                            u.emit("new-xhr", [n], n),
                            n.addEventListener(w, o, !1)
                        } catch (e) {
                            try {
                                u.emit("internal-error", [e])
                            } catch (r) {}
                        }
                        return n
                    }
                    ;
                    if (c(p, b),
                    b.prototype = p.prototype,
                    d.inPlace(b.prototype, ["open", "send"], "-xhr-", s),
                    u.on("send-xhr-start", function(t, n) {
                        r(t, n),
                        i(n)
                    }),
                    u.on("open-xhr-start", r),
                    h) {
                        var x = m && m.resolve();
                        if (!v && !m) {
                            var E = 1
                              , O = document.createTextNode(E);
                            new h(a).observe(O, {
                                characterData: !0
                            })
                        }
                    } else
                        f.on("fn-end", function(t) {
                            t[0] && t[0].type === w || a()
                        })
                }
                , {}],
                10: [function(t, n, e) {
                    function r(t) {
                        var n = this.params
                          , e = this.metrics;
                        if (!this.ended) {
                            this.ended = !0;
                            for (var r = 0; r < d; r++)
                                t.removeEventListener(u[r], this.listener, !1);
                            if (!n.aborted) {
                                if (e.duration = a.now() - this.startTime,
                                4 === t.readyState) {
                                    n.status = t.status;
                                    var i = o(t, this.lastSize);
                                    if (i && (e.rxSize = i),
                                    this.sameOrigin) {
                                        var c = t.getResponseHeader("X-NewRelic-App-Data");
                                        c && (n.cat = c.split(", ").pop())
                                    }
                                } else
                                    n.status = 0;
                                e.cbTime = this.cbTime,
                                f.emit("xhr-done", [t], t),
                                s("xhr", [n, e, this.startTime])
                            }
                        }
                    }
                    function o(t, n) {
                        var e = t.responseType;
                        if ("json" === e && null !== n)
                            return n;
                        var r = "arraybuffer" === e || "blob" === e || "json" === e ? t.response : t.responseText;
                        return h(r)
                    }
                    function i(t, n) {
                        var e = c(n)
                          , r = t.params;
                        r.host = e.hostname + ":" + e.port,
                        r.pathname = e.pathname,
                        t.sameOrigin = e.sameOrigin
                    }
                    var a = t("loader");
                    if (a.xhrWrappable) {
                        var s = t("handle")
                          , c = t(11)
                          , f = t("ee")
                          , u = ["load", "error", "abort", "timeout"]
                          , d = u.length
                          , l = t("id")
                          , p = t(14)
                          , h = t(13)
                          , m = window.XMLHttpRequest;
                        a.features.xhr = !0,
                        t(9),
                        f.on("new-xhr", function(t) {
                            var n = this;
                            n.totalCbs = 0,
                            n.called = 0,
                            n.cbTime = 0,
                            n.end = r,
                            n.ended = !1,
                            n.xhrGuids = {},
                            n.lastSize = null,
                            p && (p > 34 || p < 10) || window.opera || t.addEventListener("progress", function(t) {
                                n.lastSize = t.loaded
                            }, !1)
                        }),
                        f.on("open-xhr-start", function(t) {
                            this.params = {
                                method: t[0]
                            },
                            i(this, t[1]),
                            this.metrics = {}
                        }),
                        f.on("open-xhr-end", function(t, n) {
                            "loader_config"in NREUM && "xpid"in NREUM.loader_config && this.sameOrigin && n.setRequestHeader("X-NewRelic-ID", NREUM.loader_config.xpid)
                        }),
                        f.on("send-xhr-start", function(t, n) {
                            var e = this.metrics
                              , r = t[0]
                              , o = this;
                            if (e && r) {
                                var i = h(r);
                                i && (e.txSize = i)
                            }
                            this.startTime = a.now(),
                            this.listener = function(t) {
                                try {
                                    "abort" === t.type && (o.params.aborted = !0),
                                    ("load" !== t.type || o.called === o.totalCbs && (o.onloadCalled || "function" != typeof n.onload)) && o.end(n)
                                } catch (e) {
                                    try {
                                        f.emit("internal-error", [e])
                                    } catch (r) {}
                                }
                            }
                            ;
                            for (var s = 0; s < d; s++)
                                n.addEventListener(u[s], this.listener, !1)
                        }),
                        f.on("xhr-cb-time", function(t, n, e) {
                            this.cbTime += t,
                            n ? this.onloadCalled = !0 : this.called += 1,
                            this.called !== this.totalCbs || !this.onloadCalled && "function" == typeof e.onload || this.end(e)
                        }),
                        f.on("xhr-load-added", function(t, n) {
                            var e = "" + l(t) + !!n;
                            this.xhrGuids && !this.xhrGuids[e] && (this.xhrGuids[e] = !0,
                            this.totalCbs += 1)
                        }),
                        f.on("xhr-load-removed", function(t, n) {
                            var e = "" + l(t) + !!n;
                            this.xhrGuids && this.xhrGuids[e] && (delete this.xhrGuids[e],
                            this.totalCbs -= 1)
                        }),
                        f.on("addEventListener-end", function(t, n) {
                            n instanceof m && "load" === t[0] && f.emit("xhr-load-added", [t[1], t[2]], n)
                        }),
                        f.on("removeEventListener-end", function(t, n) {
                            n instanceof m && "load" === t[0] && f.emit("xhr-load-removed", [t[1], t[2]], n)
                        }),
                        f.on("fn-start", function(t, n, e) {
                            n instanceof m && ("onload" === e && (this.onload = !0),
                            ("load" === (t[0] && t[0].type) || this.onload) && (this.xhrCbStart = a.now()))
                        }),
                        f.on("fn-end", function(t, n) {
                            this.xhrCbStart && f.emit("xhr-cb-time", [a.now() - this.xhrCbStart, this.onload, n], n)
                        })
                    }
                }
                , {}],
                11: [function(t, n, e) {
                    n.exports = function(t) {
                        var n = document.createElement("a")
                          , e = window.location
                          , r = {};
                        n.href = t,
                        r.port = n.port;
                        var o = n.href.split("://");
                        !r.port && o[1] && (r.port = o[1].split("/")[0].split("@").pop().split(":")[1]),
                        r.port && "0" !== r.port || (r.port = "https" === o[0] ? "443" : "80"),
                        r.hostname = n.hostname || e.hostname,
                        r.pathname = n.pathname,
                        r.protocol = o[0],
                        "/" !== r.pathname.charAt(0) && (r.pathname = "/" + r.pathname);
                        var i = !n.protocol || ":" === n.protocol || n.protocol === e.protocol
                          , a = n.hostname === document.domain && n.port === e.port;
                        return r.sameOrigin = i && (!n.hostname || a),
                        r
                    }
                }
                , {}],
                12: [function(t, n, e) {
                    function r() {}
                    function o(t, n, e) {
                        return function() {
                            return i(t, [f.now()].concat(s(arguments)), n ? null : this, e),
                            n ? void 0 : this
                        }
                    }
                    var i = t("handle")
                      , a = t(16)
                      , s = t(17)
                      , c = t("ee").get("tracer")
                      , f = t("loader")
                      , u = NREUM;
                    "undefined" == typeof window.newrelic && (newrelic = u);
                    var d = ["setPageViewName", "setCustomAttribute", "setErrorHandler", "finished", "addToTrace", "inlineHit", "addRelease"]
                      , l = "api-"
                      , p = l + "ixn-";
                    a(d, function(t, n) {
                        u[n] = o(l + n, !0, "api")
                    }),
                    u.addPageAction = o(l + "addPageAction", !0),
                    u.setCurrentRouteName = o(l + "routeName", !0),
                    n.exports = newrelic,
                    u.interaction = function() {
                        return (new r).get()
                    }
                    ;
                    var h = r.prototype = {
                        createTracer: function(t, n) {
                            var e = {}
                              , r = this
                              , o = "function" == typeof n;
                            return i(p + "tracer", [f.now(), t, e], r),
                            function() {
                                if (c.emit((o ? "" : "no-") + "fn-start", [f.now(), r, o], e),
                                o)
                                    try {
                                        return n.apply(this, arguments)
                                    } catch (t) {
                                        throw c.emit("fn-err", [arguments, this, t], e),
                                        t
                                    } finally {
                                        c.emit("fn-end", [f.now()], e)
                                    }
                            }
                        }
                    };
                    a("actionText,setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","), function(t, n) {
                        h[n] = o(p + n)
                    }),
                    newrelic.noticeError = function(t, n) {
                        "string" == typeof t && (t = new Error(t)),
                        i("err", [t, f.now(), !1, n])
                    }
                }
                , {}],
                13: [function(t, n, e) {
                    n.exports = function(t) {
                        if ("string" == typeof t && t.length)
                            return t.length;
                        if ("object" == typeof t) {
                            if ("undefined" != typeof ArrayBuffer && t instanceof ArrayBuffer && t.byteLength)
                                return t.byteLength;
                            if ("undefined" != typeof Blob && t instanceof Blob && t.size)
                                return t.size;
                            if (!("undefined" != typeof FormData && t instanceof FormData))
                                try {
                                    return JSON.stringify(t).length
                                } catch (n) {
                                    return
                                }
                        }
                    }
                }
                , {}],
                14: [function(t, n, e) {
                    var r = 0
                      , o = navigator.userAgent.match(/Firefox[\/\s](\d+\.\d+)/);
                    o && (r = +o[1]),
                    n.exports = r
                }
                , {}],
                15: [function(t, n, e) {
                    function r(t, n) {
                        if (!o)
                            return !1;
                        if (t !== o)
                            return !1;
                        if (!n)
                            return !0;
                        if (!i)
                            return !1;
                        for (var e = i.split("."), r = n.split("."), a = 0; a < r.length; a++)
                            if (r[a] !== e[a])
                                return !1;
                        return !0
                    }
                    var o = null
                      , i = null
                      , a = /Version\/(\S+)\s+Safari/;
                    if (navigator.userAgent) {
                        var s = navigator.userAgent
                          , c = s.match(a);
                        c && s.indexOf("Chrome") === -1 && s.indexOf("Chromium") === -1 && (o = "Safari",
                        i = c[1])
                    }
                    n.exports = {
                        agent: o,
                        version: i,
                        match: r
                    }
                }
                , {}],
                16: [function(t, n, e) {
                    function r(t, n) {
                        var e = []
                          , r = ""
                          , i = 0;
                        for (r in t)
                            o.call(t, r) && (e[i] = n(r, t[r]),
                            i += 1);
                        return e
                    }
                    var o = Object.prototype.hasOwnProperty;
                    n.exports = r
                }
                , {}],
                17: [function(t, n, e) {
                    function r(t, n, e) {
                        n || (n = 0),
                        "undefined" == typeof e && (e = t ? t.length : 0);
                        for (var r = -1, o = e - n || 0, i = Array(o < 0 ? 0 : o); ++r < o; )
                            i[r] = t[n + r];
                        return i
                    }
                    n.exports = r
                }
                , {}],
                18: [function(t, n, e) {
                    n.exports = {
                        exists: "undefined" != typeof window.performance && window.performance.timing && "undefined" != typeof window.performance.timing.navigationStart
                    }
                }
                , {}],
                19: [function(t, n, e) {
                    function r(t) {
                        return !(t && t instanceof Function && t.apply && !t[a])
                    }
                    var o = t("ee")
                      , i = t(17)
                      , a = "nr@original"
                      , s = Object.prototype.hasOwnProperty
                      , c = !1;
                    n.exports = function(t, n) {
                        function e(t, n, e, o) {
                            function nrWrapper() {
                                var r, a, s, c;
                                try {
                                    a = this,
                                    r = i(arguments),
                                    s = "function" == typeof e ? e(r, a) : e || {}
                                } catch (f) {
                                    l([f, "", [r, a, o], s])
                                }
                                u(n + "start", [r, a, o], s);
                                try {
                                    return c = t.apply(a, r)
                                } catch (d) {
                                    throw u(n + "err", [r, a, d], s),
                                    d
                                } finally {
                                    u(n + "end", [r, a, c], s)
                                }
                            }
                            return r(t) ? t : (n || (n = ""),
                            nrWrapper[a] = t,
                            d(t, nrWrapper),
                            nrWrapper)
                        }
                        function f(t, n, o, i) {
                            o || (o = "");
                            var a, s, c, f = "-" === o.charAt(0);
                            for (c = 0; c < n.length; c++)
                                s = n[c],
                                a = t[s],
                                r(a) || (t[s] = e(a, f ? s + o : o, i, s))
                        }
                        function u(e, r, o) {
                            if (!c || n) {
                                var i = c;
                                c = !0;
                                try {
                                    t.emit(e, r, o, n)
                                } catch (a) {
                                    l([a, e, r, o])
                                }
                                c = i
                            }
                        }
                        function d(t, n) {
                            if (Object.defineProperty && Object.keys)
                                try {
                                    var e = Object.keys(t);
                                    return e.forEach(function(e) {
                                        Object.defineProperty(n, e, {
                                            get: function() {
                                                return t[e]
                                            },
                                            set: function(n) {
                                                return t[e] = n,
                                                n
                                            }
                                        })
                                    }),
                                    n
                                } catch (r) {
                                    l([r])
                                }
                            for (var o in t)
                                s.call(t, o) && (n[o] = t[o]);
                            return n
                        }
                        function l(n) {
                            try {
                                t.emit("internal-error", n)
                            } catch (e) {}
                        }
                        return t || (t = o),
                        e.inPlace = f,
                        e.flag = a,
                        e
                    }
                }
                , {}],
                ee: [function(t, n, e) {
                    function r() {}
                    function o(t) {
                        function n(t) {
                            return t && t instanceof r ? t : t ? c(t, s, i) : i()
                        }
                        function e(e, r, o, i) {
                            if (!l.aborted || i) {
                                t && t(e, r, o);
                                for (var a = n(o), s = m(e), c = s.length, f = 0; f < c; f++)
                                    s[f].apply(a, r);
                                var d = u[g[e]];
                                return d && d.push([b, e, r, a]),
                                a
                            }
                        }
                        function p(t, n) {
                            y[t] = m(t).concat(n)
                        }
                        function h(t, n) {
                            var e = y[t];
                            if (e)
                                for (var r = 0; r < e.length; r++)
                                    e[r] === n && e.splice(r, 1)
                        }
                        function m(t) {
                            return y[t] || []
                        }
                        function v(t) {
                            return d[t] = d[t] || o(e)
                        }
                        function w(t, n) {
                            f(t, function(t, e) {
                                n = n || "feature",
                                g[e] = n,
                                n in u || (u[n] = [])
                            })
                        }
                        var y = {}
                          , g = {}
                          , b = {
                            on: p,
                            addEventListener: p,
                            removeEventListener: h,
                            emit: e,
                            get: v,
                            listeners: m,
                            context: n,
                            buffer: w,
                            abort: a,
                            aborted: !1
                        };
                        return b
                    }
                    function i() {
                        return new r
                    }
                    function a() {
                        (u.api || u.feature) && (l.aborted = !0,
                        u = l.backlog = {})
                    }
                    var s = "nr@context"
                      , c = t("gos")
                      , f = t(16)
                      , u = {}
                      , d = {}
                      , l = n.exports = o();
                    l.backlog = u
                }
                , {}],
                gos: [function(t, n, e) {
                    function r(t, n, e) {
                        if (o.call(t, n))
                            return t[n];
                        var r = e();
                        if (Object.defineProperty && Object.keys)
                            try {
                                return Object.defineProperty(t, n, {
                                    value: r,
                                    writable: !0,
                                    enumerable: !1
                                }),
                                r
                            } catch (i) {}
                        return t[n] = r,
                        r
                    }
                    var o = Object.prototype.hasOwnProperty;
                    n.exports = r
                }
                , {}],
                handle: [function(t, n, e) {
                    function r(t, n, e, r) {
                        o.buffer([t], r),
                        o.emit(t, n, e)
                    }
                    var o = t("ee").get("handle");
                    n.exports = r,
                    r.ee = o
                }
                , {}],
                id: [function(t, n, e) {
                    function r(t) {
                        var n = typeof t;
                        return !t || "object" !== n && "function" !== n ? -1 : t === window ? 0 : a(t, i, function() {
                            return o++
                        })
                    }
                    var o = 1
                      , i = "nr@id"
                      , a = t("gos");
                    n.exports = r
                }
                , {}],
                loader: [function(t, n, e) {
                    function r() {
                        if (!E++) {
                            var t = x.info = NREUM.info
                              , n = p.getElementsByTagName("script")[0];
                            if (setTimeout(u.abort, 3e4),
                            !(t && t.licenseKey && t.applicationID && n))
                                return u.abort();
                            f(g, function(n, e) {
                                t[n] || (t[n] = e)
                            }),
                            c("mark", ["onload", a() + x.offset], null, "api");
                            var e = p.createElement("script");
                            e.src = "https://" + t.agent,
                            n.parentNode.insertBefore(e, n)
                        }
                    }
                    function o() {
                        "complete" === p.readyState && i()
                    }
                    function i() {
                        c("mark", ["domContent", a() + x.offset], null, "api")
                    }
                    function a() {
                        return O.exists && performance.now ? Math.round(performance.now()) : (s = Math.max((new Date).getTime(), s)) - x.offset
                    }
                    var s = (new Date).getTime()
                      , c = t("handle")
                      , f = t(16)
                      , u = t("ee")
                      , d = t(15)
                      , l = window
                      , p = l.document
                      , h = "addEventListener"
                      , m = "attachEvent"
                      , v = l.XMLHttpRequest
                      , w = v && v.prototype;
                    NREUM.o = {
                        ST: setTimeout,
                        SI: l.setImmediate,
                        CT: clearTimeout,
                        XHR: v,
                        REQ: l.Request,
                        EV: l.Event,
                        PR: l.Promise,
                        MO: l.MutationObserver
                    };
                    var y = "" + location
                      , g = {
                        beacon: "bam.nr-data.net",
                        errorBeacon: "bam.nr-data.net",
                        agent: "js-agent.newrelic.com/nr-1118.min.js"
                    }
                      , b = v && w && w[h] && !/CriOS/.test(navigator.userAgent)
                      , x = n.exports = {
                        offset: s,
                        now: a,
                        origin: y,
                        features: {},
                        xhrWrappable: b,
                        userAgent: d
                    };
                    t(12),
                    p[h] ? (p[h]("DOMContentLoaded", i, !1),
                    l[h]("load", r, !1)) : (p[m]("onreadystatechange", o),
                    l[m]("onload", r)),
                    c("mark", ["firstbyte", s], null, "api");
                    var E = 0
                      , O = t(18)
                }
                , {}]
            }, {}, ["loader", 2, 10, 4, 3]);
        </script>
        <meta name="Generator" content="Drupal 7 (http://drupal.org)"/>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <title>myStevens | Online Services for the Stevens Community</title>
        <style type="text/css" media="all">
            @import url("https://my.stevens.edu/modules/system/system.base.css?pm2omv"); @import url("https://my.stevens.edu/modules/system/system.messages.css?pm2omv"); @import url("https://my.stevens.edu/modules/system/system.theme.css?pm2omv"); </style>
        <style type="text/css" media="all">
            @import url("https://my.stevens.edu/profiles/openatrium/themes/oa_basetheme/assets/vendor/jqueryui/jquery-ui-1.10.0.custom.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/contrib/jquery_update/replace/ui/themes/base/minified/jquery.ui.accordion.min.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/contrib/media/css/media.css?pm2omv"); </style>
        <style type="text/css" media="all">
            @import url("https://my.stevens.edu/modules/comment/comment.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/contrib/contextual_tabs/contextual_tabs.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/contrib/date/date_api/date.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/contrib/date/date_popup/themes/datepicker.1.7.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/contrib/date/date_repeat_field/date_repeat_field.css?pm2omv"); @import url("https://my.stevens.edu/modules/field/theme/field.css?pm2omv"); @import url("https://my.stevens.edu/sites/all/modules/contrib/google_cse/google_cse.css?pm2omv"); @import url("https://my.stevens.edu/modules/node/node.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/apps/oa_appearance/oa_appearance.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/contrib/oa_core/css/oa_core.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/apps/oa_events/oa-events.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/apps/oa_favorites/oa_favorites.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/apps/oa_media/oa_media.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/apps/oa_related/oa_related.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/contrib/oa_core/modules/oa_river/oa_river.css?pm2omv"); </style>
        <style type="text/css" media="screen">
            @import url("https://my.stevens.edu/profiles/openatrium/modules/apps/oa_subspaces/oa-subspaces.css?pm2omv"); </style>
        <style type="text/css" media="all">
            @import url("https://my.stevens.edu/profiles/openatrium/modules/contrib/oa_core/modules/oa_teams/oa_teams.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/apps/oa_toolbar/css/oa_toolbar.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/contrib/oa_core/modules/oa_widgets/oa_widgets.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/apps/oa_wiki/oa_wiki.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/apps/oa_worktracker/oa_worktracker.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/panopoly/panopoly_admin/panopoly-admin-navbar.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/panopoly/panopoly_core/css/panopoly-dropbutton.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/panopoly/panopoly_magic/css/panopoly-magic.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/panopoly/panopoly_theme/css/panopoly-featured.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/panopoly/panopoly_theme/css/panopoly-accordian.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/panopoly/panopoly_theme/css/panopoly-layouts.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/panopoly/panopoly_widgets/panopoly-widgets.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/panopoly/panopoly_widgets/panopoly-widgets-spotlight.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/panopoly/panopoly_wysiwyg/panopoly-wysiwyg.css?pm2omv"); @import url("https://my.stevens.edu/modules/poll/poll.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/contrib/radix_layouts/radix_layouts.css?pm2omv"); @import url("https://my.stevens.edu/modules/search/search.css?pm2omv"); @import url("https://my.stevens.edu/modules/user/user.css?pm2omv"); @import url("https://my.stevens.edu/sites/all/modules/contrib/extlink/extlink.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/contrib/views/css/views.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/contrib/caption_filter/caption-filter.css?pm2omv"); </style>
        <style type="text/css" media="all">
            @import url("https://my.stevens.edu/profiles/openatrium/modules/contrib/colorbox/styles/default/colorbox_style.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/contrib/ctools/css/ctools.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/contrib/dhtml_menu/dhtml_menu.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/contrib/oa_core/modules/oa_diff/oa_diff.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/contrib/panels/css/panels.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/contrib/panelizer/css/panelizer-ipe.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/contrib/oa_responsive_regions/css/oa_responsive_regions.css?pm2omv"); @import url("https://my.stevens.edu/sites/default/modules/custom/stevens_mystevens_feedback/feedback.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/apps/oa_tour/oa_tour.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/apps/oa_search/oa_search.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/modules/apps/oa_site_layout/oa_site_layout.css?pm2omv"); </style>
        <style type="text/css" media="all">
            @import url("https://my.stevens.edu/profiles/openatrium/themes/oa_basetheme/assets/css/fontawesome_3.2.1.css?pm2omv"); @import url("https://my.stevens.edu/profiles/openatrium/themes/oa_basetheme/assets/css/oa_basetheme.style.css?pm2omv"); @import url("https://my.stevens.edu/sites/default/themes/stevens_contempo/assets/css/stevens_contempo.style.css?pm2omv"); </style>
        <style type="text/css" media="print">
            @import url("https://my.stevens.edu/sites/default/themes/stevens_contempo/assets/css/print.css?pm2omv"); </style>
        <link type="text/css" rel="stylesheet" href="https://my.stevens.edu/sites/default/files/colorizer/stevens_contempo-bcd0380a.css" media="all"/>
        <style type="text/css" media="all">
            @import url("https://my.stevens.edu/profiles/openatrium/modules/panopoly/panopoly_images/panopoly-images.css?pm2omv"); </style>
        <script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
        <script type="text/javascript">
            <!--//--><![CDATA[//><!--
            window.jQuery || document.write("<script src='/profiles/openatrium/modules/contrib/jquery_update/replace/jquery/1.7/jquery.min.js'>\x3C/script>")
            //--><!]]>
        </script>
        <script type="text/javascript" src="https://my.stevens.edu/misc/jquery.once.js?v=1.2"></script>
        <script type="text/javascript" src="https://my.stevens.edu/misc/drupal.js?pm2omv"></script>
        <script type="text/javascript" src="https://my.stevens.edu/profiles/openatrium/libraries/bootstrap/js/bootstrap.min.js?pm2omv"></script>
        <script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js"></script>
        <script type="text/javascript">
            <!--//--><![CDATA[//><!--
            window.jQuery.ui || document.write("<script src='/profiles/openatrium/modules/contrib/jquery_update/replace/ui/ui/minified/jquery-ui.min.js'>\x3C/script>")
            //--><!]]>
        </script>
        <script type="text/javascript" src="https://my.stevens.edu/profiles/openatrium/modules/contrib/media/js/media.core.js?v=7.x-2.0-beta1"></script>
        <script type="text/javascript" src="https://my.stevens.edu/profiles/openatrium/modules/contrib/jquery_update/replace/ui/external/jquery.cookie.js?v=67fb34f6a866c40d0570"></script>
        <script type="text/javascript" src="https://my.stevens.edu/profiles/openatrium/modules/contrib/jquery_update/replace/misc/jquery.form.min.js?v=2.69"></script>
        <script type="text/javascript" src="https://my.stevens.edu/profiles/openatrium/modules/contrib/panelizer/js/panelizer-ipe.js?pm2omv"></script>
        <script type="text/javascript" src="https://my.stevens.edu/profiles/openatrium/modules/contrib/media/js/util/json2.js?v=7.x-2.0-beta1"></script>
        <script type="text/javascript" src="https://my.stevens.edu/profiles/openatrium/modules/contrib/media/js/util/ba-debug.min.js?v=7.x-2.0-beta1"></script>
        <script type="text/javascript" src="https://my.stevens.edu/misc/ajax.js?v=7.61"></script>
        <script type="text/javascript" src="https://my.stevens.edu/profiles/openatrium/modules/contrib/jquery_update/js/jquery_update.js?v=0.0.1"></script>
        <script type="text/javascript" src="https://my.stevens.edu/profiles/openatrium/modules/panopoly/panopoly_images/panopoly-images.js?pm2omv"></script>
        <script type="text/javascript" src="https://my.stevens.edu/sites/all/modules/contrib/google_cse/google_cse.js?pm2omv"></script>
        <script type="text/javascript" src="https://my.stevens.edu/profiles/openatrium/modules/contrib/media_colorbox/media_colorbox.js?pm2omv"></script>
        <script type="text/javascript" src="https://my.stevens.edu/profiles/openatrium/modules/panopoly/panopoly_admin/panopoly-admin.js?pm2omv"></script>
        <script type="text/javascript" src="https://my.stevens.edu/profiles/openatrium/modules/panopoly/panopoly_magic/panopoly-magic.js?pm2omv"></script>
        <script type="text/javascript" src="https://my.stevens.edu/profiles/openatrium/modules/panopoly/panopoly_theme/js/panopoly-accordion.js?pm2omv"></script>
        <script type="text/javascript" src="https://my.stevens.edu/sites/all/modules/contrib/extlink/extlink.js?pm2omv"></script>
        <script type="text/javascript" src="https://my.stevens.edu/profiles/openatrium/modules/contrib/caption_filter/js/caption-filter.js?pm2omv"></script>
        <script type="text/javascript" src="https://my.stevens.edu/profiles/openatrium/libraries/colorbox/jquery.colorbox-min.js?pm2omv"></script>
        <script type="text/javascript" src="https://my.stevens.edu/profiles/openatrium/modules/contrib/colorbox/js/colorbox.js?pm2omv"></script>
        <script type="text/javascript" src="https://my.stevens.edu/profiles/openatrium/modules/contrib/colorbox/styles/default/colorbox_style.js?pm2omv"></script>
        <script type="text/javascript" src="https://my.stevens.edu/profiles/openatrium/modules/contrib/dhtml_menu/dhtml_menu.js?pm2omv"></script>
        <script type="text/javascript" src="https://my.stevens.edu/sites/all/modules/contrib/memcache/memcache_admin/memcache.js?pm2omv"></script>
        <script type="text/javascript" src="https://my.stevens.edu/profiles/openatrium/libraries/jquery.imagesloaded/jquery.imagesloaded.min.js?pm2omv"></script>
        <script type="text/javascript" src="https://my.stevens.edu/sites/default/modules/custom/stevens_mystevens_flexslider_link/js/flexslider_link.js?pm2omv"></script>
        <script type="text/javascript" src="https://my.stevens.edu/profiles/openatrium/modules/contrib/views_load_more/views_load_more.js?pm2omv"></script>
        <script type="text/javascript">
            <!--//--><![CDATA[//><!--
            (function($) {
                $(function() {
                    jQuery(".pane-content").on("DOMSubtreeModified propertychange", "#twitter-widget-0", function() {
                        jQuery(".twitter-timeline").contents().find(".timeline-Tweet-media").css("display", "none");
                        jQuery(".pane-content").css("height", "100%");
                    });
                });
            }
            )(jQuery);
            //--><!]]>
        </script>
        <script type="text/javascript" src="https://my.stevens.edu/sites/default/modules/custom/stevens_mystevens_detect_network/stevens_mystevens_detect_network.js?pm2omv"></script>
        <script type="text/javascript" src="https://my.stevens.edu/sites/default/modules/custom/stevens_mystevens_api_badge/stevens_mystevens_api_badge.js?pm2omv"></script>
        <script type="text/javascript" src="https://my.stevens.edu/profiles/openatrium/modules/contrib/oa_responsive_regions/js/oa_responsive_regions.js?pm2omv"></script>
        <script type="text/javascript" src="https://my.stevens.edu/profiles/openatrium/modules/contrib/media/js/media.popups.js?v=7.x-2.0-beta1"></script>
        <script type="text/javascript" src="https://my.stevens.edu/misc/progress.js?v=7.61"></script>
        <script type="text/javascript" src="https://my.stevens.edu/profiles/openatrium/modules/apps/oa_files/js/upload.js?pm2omv"></script>
        <script type="text/javascript" src="https://my.stevens.edu/sites/default/modules/custom/stevens_mystevens_feedback/feedback.js?pm2omv"></script>
        <script type="text/javascript" src="https://my.stevens.edu/profiles/openatrium/modules/apps/oa_search/js/oa_search.js?pm2omv"></script>
        <script type="text/javascript" src="https://my.stevens.edu/profiles/openatrium/modules/apps/oa_appearance/oa_appearance.js?pm2omv"></script>
        <script type="text/javascript" src="https://my.stevens.edu/profiles/openatrium/modules/apps/oa_toolbar/js/oa-toolbar.js?pm2omv"></script>
        <script type="text/javascript" src="https://my.stevens.edu/profiles/openatrium/themes/oa_basetheme/assets/js/radix.script.js?pm2omv"></script>
        <script type="text/javascript" src="https://my.stevens.edu/profiles/openatrium/themes/oa_basetheme/assets/js/oa_basetheme.script.min.js?pm2omv"></script>
        <script type="text/javascript" src="https://my.stevens.edu/sites/default/themes/stevens_contempo/assets/js/stevens_contempo.script.min.js?pm2omv"></script>
        <script type="text/javascript" src="https://my.stevens.edu/profiles/openatrium/themes/oa_basetheme/assets/js/oa_basetheme.progress.js?pm2omv"></script>
        <script type="text/javascript">
            <!--//--><![CDATA[//><!--
            jQuery.extend(Drupal.settings, {
                "basePath": "\/",
                "pathPrefix": "",
                "ajaxPageState": {
                    "theme": "stevens_contempo",
                    "theme_token": "KeS5al3gCU0lRcgTh0p3H7aModImeARbyrk35tYcROw",
                    "jquery_version": "1.7",
                    "js": {
                        "profiles\/openatrium\/modules\/panopoly\/panopoly_widgets\/panopoly-widgets.js": 1,
                        "profiles\/openatrium\/modules\/panopoly\/panopoly_widgets\/panopoly-widgets-spotlight.js": 1,
                        "\/\/ajax.googleapis.com\/ajax\/libs\/jquery\/1.7.2\/jquery.min.js": 1,
                        "0": 1,
                        "misc\/jquery.once.js": 1,
                        "misc\/drupal.js": 1,
                        "profiles\/openatrium\/libraries\/bootstrap\/js\/bootstrap.min.js": 1,
                        "\/\/ajax.googleapis.com\/ajax\/libs\/jqueryui\/1.10.2\/jquery-ui.min.js": 1,
                        "1": 1,
                        "profiles\/openatrium\/modules\/contrib\/media\/js\/media.core.js": 1,
                        "profiles\/openatrium\/modules\/contrib\/jquery_update\/replace\/ui\/external\/jquery.cookie.js": 1,
                        "profiles\/openatrium\/modules\/contrib\/jquery_update\/replace\/misc\/jquery.form.min.js": 1,
                        "profiles\/openatrium\/modules\/contrib\/panelizer\/js\/panelizer-ipe.js": 1,
                        "profiles\/openatrium\/modules\/contrib\/media\/js\/util\/json2.js": 1,
                        "profiles\/openatrium\/modules\/contrib\/media\/js\/util\/ba-debug.min.js": 1,
                        "misc\/ajax.js": 1,
                        "profiles\/openatrium\/modules\/contrib\/jquery_update\/js\/jquery_update.js": 1,
                        "profiles\/openatrium\/modules\/panopoly\/panopoly_images\/panopoly-images.js": 1,
                        "sites\/all\/modules\/contrib\/google_cse\/google_cse.js": 1,
                        "profiles\/openatrium\/modules\/contrib\/media_colorbox\/media_colorbox.js": 1,
                        "profiles\/openatrium\/modules\/panopoly\/panopoly_admin\/panopoly-admin.js": 1,
                        "profiles\/openatrium\/modules\/panopoly\/panopoly_magic\/panopoly-magic.js": 1,
                        "profiles\/openatrium\/modules\/panopoly\/panopoly_theme\/js\/panopoly-accordion.js": 1,
                        "sites\/all\/modules\/contrib\/extlink\/extlink.js": 1,
                        "profiles\/openatrium\/modules\/contrib\/caption_filter\/js\/caption-filter.js": 1,
                        "profiles\/openatrium\/libraries\/colorbox\/jquery.colorbox-min.js": 1,
                        "profiles\/openatrium\/modules\/contrib\/colorbox\/js\/colorbox.js": 1,
                        "profiles\/openatrium\/modules\/contrib\/colorbox\/styles\/default\/colorbox_style.js": 1,
                        "profiles\/openatrium\/modules\/contrib\/dhtml_menu\/dhtml_menu.js": 1,
                        "sites\/all\/modules\/contrib\/memcache\/memcache_admin\/memcache.js": 1,
                        "profiles\/openatrium\/libraries\/jquery.imagesloaded\/jquery.imagesloaded.min.js": 1,
                        "sites\/default\/modules\/custom\/stevens_mystevens_flexslider_link\/js\/flexslider_link.js": 1,
                        "profiles\/openatrium\/modules\/contrib\/views_load_more\/views_load_more.js": 1,
                        "2": 1,
                        "sites\/default\/modules\/custom\/stevens_mystevens_detect_network\/stevens_mystevens_detect_network.js": 1,
                        "sites\/default\/modules\/custom\/stevens_mystevens_api_badge\/stevens_mystevens_api_badge.js": 1,
                        "profiles\/openatrium\/modules\/contrib\/oa_responsive_regions\/js\/oa_responsive_regions.js": 1,
                        "profiles\/openatrium\/modules\/contrib\/media\/js\/media.popups.js": 1,
                        "misc\/progress.js": 1,
                        "profiles\/openatrium\/modules\/apps\/oa_files\/js\/upload.js": 1,
                        "sites\/default\/modules\/custom\/stevens_mystevens_feedback\/feedback.js": 1,
                        "profiles\/openatrium\/modules\/apps\/oa_search\/js\/oa_search.js": 1,
                        "profiles\/openatrium\/modules\/apps\/oa_appearance\/oa_appearance.js": 1,
                        "profiles\/openatrium\/modules\/apps\/oa_toolbar\/js\/oa-toolbar.js": 1,
                        "profiles\/openatrium\/themes\/oa_basetheme\/assets\/js\/radix.script.js": 1,
                        "profiles\/openatrium\/themes\/oa_basetheme\/assets\/js\/oa_basetheme.script.min.js": 1,
                        "sites\/default\/themes\/stevens_contempo\/assets\/js\/stevens_contempo.script.min.js": 1,
                        "profiles\/openatrium\/themes\/oa_basetheme\/assets\/js\/oa_basetheme.progress.js": 1
                    },
                    "css": {
                        "modules\/system\/system.base.css": 1,
                        "modules\/system\/system.messages.css": 1,
                        "modules\/system\/system.theme.css": 1,
                        "misc\/ui\/jquery.ui.theme.css": 1,
                        "misc\/ui\/jquery.ui.accordion.css": 1,
                        "profiles\/openatrium\/modules\/contrib\/media\/css\/media.css": 1,
                        "modules\/comment\/comment.css": 1,
                        "profiles\/openatrium\/modules\/contrib\/contextual_tabs\/contextual_tabs.css": 1,
                        "profiles\/openatrium\/modules\/contrib\/date\/date_api\/date.css": 1,
                        "profiles\/openatrium\/modules\/contrib\/date\/date_popup\/themes\/datepicker.1.7.css": 1,
                        "profiles\/openatrium\/modules\/contrib\/date\/date_repeat_field\/date_repeat_field.css": 1,
                        "modules\/field\/theme\/field.css": 1,
                        "sites\/all\/modules\/contrib\/google_cse\/google_cse.css": 1,
                        "modules\/node\/node.css": 1,
                        "profiles\/openatrium\/modules\/apps\/oa_appearance\/oa_appearance.css": 1,
                        "profiles\/openatrium\/modules\/contrib\/oa_core\/css\/oa_core.css": 1,
                        "profiles\/openatrium\/modules\/apps\/oa_events\/oa-events.css": 1,
                        "profiles\/openatrium\/modules\/apps\/oa_favorites\/oa_favorites.css": 1,
                        "profiles\/openatrium\/modules\/apps\/oa_media\/oa_media.css": 1,
                        "profiles\/openatrium\/modules\/apps\/oa_related\/oa_related.css": 1,
                        "profiles\/openatrium\/modules\/contrib\/oa_core\/modules\/oa_river\/oa_river.css": 1,
                        "profiles\/openatrium\/modules\/contrib\/oa_core\/modules\/oa_sections\/oa_sections.css": 1,
                        "profiles\/openatrium\/modules\/apps\/oa_subspaces\/oa-subspaces.css": 1,
                        "profiles\/openatrium\/modules\/contrib\/oa_core\/modules\/oa_teams\/oa_teams.css": 1,
                        "profiles\/openatrium\/modules\/apps\/oa_toolbar\/css\/oa_toolbar.css": 1,
                        "profiles\/openatrium\/modules\/contrib\/oa_core\/modules\/oa_widgets\/oa_widgets.css": 1,
                        "profiles\/openatrium\/modules\/apps\/oa_wiki\/oa_wiki.css": 1,
                        "profiles\/openatrium\/modules\/apps\/oa_worktracker\/oa_worktracker.css": 1,
                        "profiles\/openatrium\/modules\/panopoly\/panopoly_admin\/panopoly-admin-navbar.css": 1,
                        "profiles\/openatrium\/modules\/panopoly\/panopoly_core\/css\/panopoly-dropbutton.css": 1,
                        "profiles\/openatrium\/modules\/panopoly\/panopoly_magic\/css\/panopoly-magic.css": 1,
                        "profiles\/openatrium\/modules\/panopoly\/panopoly_theme\/css\/panopoly-featured.css": 1,
                        "profiles\/openatrium\/modules\/panopoly\/panopoly_theme\/css\/panopoly-accordian.css": 1,
                        "profiles\/openatrium\/modules\/panopoly\/panopoly_theme\/css\/panopoly-layouts.css": 1,
                        "profiles\/openatrium\/modules\/panopoly\/panopoly_widgets\/panopoly-widgets.css": 1,
                        "profiles\/openatrium\/modules\/panopoly\/panopoly_widgets\/panopoly-widgets-spotlight.css": 1,
                        "profiles\/openatrium\/modules\/panopoly\/panopoly_wysiwyg\/panopoly-wysiwyg.css": 1,
                        "modules\/poll\/poll.css": 1,
                        "profiles\/openatrium\/modules\/contrib\/radix_layouts\/radix_layouts.css": 1,
                        "modules\/search\/search.css": 1,
                        "modules\/user\/user.css": 1,
                        "sites\/all\/modules\/contrib\/extlink\/extlink.css": 1,
                        "profiles\/openatrium\/modules\/contrib\/views\/css\/views.css": 1,
                        "profiles\/openatrium\/modules\/contrib\/caption_filter\/caption-filter.css": 1,
                        "profiles\/openatrium\/modules\/contrib\/colorbox\/styles\/default\/colorbox_style.css": 1,
                        "profiles\/openatrium\/modules\/contrib\/ctools\/css\/ctools.css": 1,
                        "profiles\/openatrium\/modules\/contrib\/dhtml_menu\/dhtml_menu.css": 1,
                        "profiles\/openatrium\/modules\/contrib\/oa_core\/modules\/oa_diff\/oa_diff.css": 1,
                        "profiles\/openatrium\/modules\/contrib\/panels\/css\/panels.css": 1,
                        "profiles\/openatrium\/modules\/contrib\/panelizer\/css\/panelizer-ipe.css": 1,
                        "profiles\/openatrium\/modules\/contrib\/oa_responsive_regions\/css\/oa_responsive_regions.css": 1,
                        "sites\/default\/modules\/custom\/stevens_mystevens_feedback\/feedback.css": 1,
                        "profiles\/openatrium\/modules\/apps\/oa_tour\/oa_tour.css": 1,
                        "profiles\/openatrium\/modules\/apps\/oa_search\/oa_search.css": 1,
                        "profiles\/openatrium\/modules\/apps\/oa_site_layout\/oa_site_layout.css": 1,
                        "profiles\/openatrium\/themes\/oa_basetheme\/assets\/css\/fontawesome_3.2.1.css": 1,
                        "profiles\/openatrium\/themes\/oa_basetheme\/assets\/css\/oa_basetheme.style.css": 1,
                        "sites\/default\/themes\/stevens_contempo\/assets\/css\/stevens_contempo.style.css": 1,
                        "sites\/default\/themes\/stevens_contempo\/assets\/css\/print.css": 1,
                        "https:\/\/my.stevens.edu\/sites\/default\/files\/colorizer\/stevens_contempo-bcd0380a.css": 1,
                        "profiles\/openatrium\/modules\/panopoly\/panopoly_images\/panopoly-images.css": 1
                    }
                },
                "colorbox": {
                    "transition": "elastic",
                    "speed": "350",
                    "opacity": "0.85",
                    "slideshow": false,
                    "slideshowAuto": true,
                    "slideshowSpeed": "2500",
                    "slideshowStart": "start slideshow",
                    "slideshowStop": "stop slideshow",
                    "current": "{current} of {total}",
                    "previous": "\u00ab Prev",
                    "next": "Next \u00bb",
                    "close": "Close",
                    "overlayClose": true,
                    "maxWidth": "98%",
                    "maxHeight": "95%",
                    "initialWidth": "300",
                    "initialHeight": "250",
                    "fixed": true,
                    "scrolling": true,
                    "mobiledetect": true,
                    "mobiledevicewidth": "480px"
                },
                "dhtmlMenu": {
                    "nav": "none",
                    "animation": {
                        "effects": {
                            "height": "height",
                            "opacity": "opacity",
                            "width": 0
                        },
                        "speed": "100"
                    },
                    "effects": {
                        "siblings": "none",
                        "children": "none",
                        "remember": "remember"
                    },
                    "filter": {
                        "type": "whitelist",
                        "list": {
                            "main-menu": "main-menu",
                            "menu-duckbill": "menu-duckbill",
                            "menu-information-technology-menu": "menu-information-technology-menu",
                            "navigation": "navigation",
                            "og-menu-single": "og-menu-single",
                            "shortcut-set-1": "shortcut-set-1",
                            "user-menu": "user-menu",
                            "management": 0,
                            "menu-academic-support-center": 0,
                            "menu-faculty-senate-menu": 0,
                            "menu-incoming-freshman-class-of-": 0,
                            "menu-student-service-center": 0
                        }
                    }
                },
                "googleCSE": {
                    "cx": "001121190494222698426:1_dk_pysrr0",
                    "language": "",
                    "resultsWidth": 600,
                    "domain": "www.google.com",
                    "showWaterMark": 1
                },
                "CToolsModal": {
                    "modalSize": {
                        "type": "scale",
                        "width": ".9",
                        "height": ".9",
                        "addWidth": 0,
                        "addHeight": 0,
                        "contentRight": 25,
                        "contentBottom": 75
                    },
                    "modalOptions": {
                        "opacity": ".55",
                        "background-color": "#FFF"
                    },
                    "animationSpeed": "fast",
                    "modalTheme": "CToolsModalDialog",
                    "throbberTheme": "CToolsModalThrobber"
                },
                "panopoly_magic": {
                    "pane_add_preview_mode": "disabled"
                },
                "views": {
                    "ajax_path": "\/views\/ajax",
                    "ajaxViews": {
                        "views_dom_id:b3af1a558d0f9b6c50d5d821a9121232": {
                            "view_name": "stevens_mystevens_events_by_channel",
                            "view_display_id": "upcoming_events_small",
                            "view_args": "",
                            "view_path": "node\/12441",
                            "view_base_path": null,
                            "view_dom_id": "b3af1a558d0f9b6c50d5d821a9121232",
                            "pager_element": 0
                        }
                    }
                },
                "stevens_esp": {
                    "badgeEndpoints": {
                        "7c62b5bd-8404-49db-a8af-914a92af5fe3": "canvas",
                        "d30d2b53-dbc1-41a1-86e2-b844232979cd": "workday",
                        "61d9de39-799d-4c47-9bab-8a9fb53d5cc0": "td"
                    },
                    "creds": {
                        "username": "msimpkin",
                        "cwid": "10433170",
                        "hash": "5805613551a400d1263242fc9cb42aa4a673a44a427e78bfc64a0c62add795d0"
                    },
                    "pollingInterval": 60000
                },
                "extlink": {
                    "extTarget": "_blank",
                    "extClass": "ext",
                    "extLabel": "(link is external)",
                    "extImgClass": 0,
                    "extSubdomains": 0,
                    "extExclude": "",
                    "extInclude": "\\.(pdf|doc|docx|xls|xlsx)$",
                    "extCssExclude": ".page-node-56",
                    "extCssExplicit": "",
                    "extAlert": 0,
                    "extAlertText": "This link will take you to an external web site.",
                    "mailtoClass": "mailto",
                    "mailtoLabel": "(link sends e-mail)"
                },
                "media": {
                    "browserUrl": "\/media\/browser?render=media-popup",
                    "styleSelectorUrl": "\/media\/-media_id-\/format-form?render=media-popup",
                    "dialogOptions": {
                        "dialogclass": "media-wrapper",
                        "modal": false,
                        "draggable": false,
                        "resizable": false,
                        "minwidth": 500,
                        "width": 670,
                        "height": 280,
                        "position": "center",
                        "overlay": {
                            "backgroundcolor": "#000000",
                            "opacity": 0.40000000000000002
                        },
                        "zindex": 10000
                    }
                },
                "oa_files_media_options": {
                    "global": {
                        "types": {
                            "document": "document",
                            "image": "image",
                            "video": "video"
                        },
                        "enabledPlugins": {
                            "media_default--media_browser_1": "media_default--media_browser_1",
                            "media_default--media_browser_my_files": "media_default--media_browser_my_files",
                            "media_internet": "media_internet",
                            "upload": "upload"
                        },
                        "schemes": {
                            "private": "private",
                            "public": "public",
                            "vimeo": "vimeo",
                            "youtube": "youtube"
                        },
                        "file_directory": "",
                        "file_extensions": "jpg jpeg gif png txt doc docx xls xlsx pdf ppt pptx pps ppsx odt ods odp mp3 mov mp4 m4a m4v mpeg avi ogg oga ogv weba webp webm ico html htm",
                        "max_filesize": 0,
                        "uri_scheme": "private",
                        "multiselect": true
                    }
                },
                "oa_files_upload_url": "\/oa-files\/upload\/multi",
                "oa_search": {
                    "space": "myStevens Portal"
                },
                "oa_toolbar": {
                    "mouseover": 1
                },
                "ogContext": {
                    "groupType": "node",
                    "gid": "12446"
                }
            });
            //--><!]]>
        </script>
        <!--[if lt IE 9]>
   <script>
      document.createElement('header');
      document.createElement('nav');
      document.createElement('section');
      document.createElement('article');
      document.createElement('aside');
      document.createElement('footer');
   </script>
  <![endif]-->
    </head>
    <body class="html front logged-in no-sidebars page-node page-node- page-node-12441 node-type-panopoly-page oa-main-menu oa-no-page-title og-context og-context-node og-context-node-12446 node-promoted  region-content panel-layout-oa_site_layout panel-region-content panel-region-contentheader panel-region-footer panel-region-header panel-region-sidebar1 panel-region-traybottom panel-region-traytop">
        <div id="skip-link">
            <a href="#main" class="element-invisible element-focusable">Skip to main content</a>
        </div>
        <div class="panel-display oa-site-layout-default clearfix oa-site-layout">
            <div class="container-fluid oa-flex-column">
                <div class="row">
                    <div class="col-md-12 oa-layout-traytop panel-panel">
                        <div class="panel-panel-inner">
                            <div class="oa-responsive-region oa-responsive-desktop oa-responsive-region-top oa-responsive-fixed oa-responsive-expand " data-position="top">
                                <div class="oa-responsive-region-inner"></div>
                            </div>
                            <div class="oa-hidden " data-position="top">
                                <div class="oa-responsive-region-inner"></div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <header class="col-md-12 oa-layout-header panel-panel">
                        <div class="panel-panel-inner">
                            <div class="oa-horizontal-slice style-region oa-fullwidth">
                                <div class="panel-pane pane-oa-space-banner">
                                    <div class="pane-content">
                                        <div class='oa-banner oa-banner-before oa-banner-nostretch' data-width='0' data-height='52'>
                                            <a href="/">
                                                <img class="oa-banner-img" src="https://my.stevens.edu/sites/default/files/mystevens-new.png" width="251" height="52" alt="Site banner"/>
                                            </a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="oa-horizontal-slice style-region oa-toolbar-style navbar navbar-inverse oa-fullwidth">
                                <div class="panel-pane pane-panels-mini pane-oa-toolbar-modern-panel oa-navbar">
                                    <div class="pane-content">
                                        <div class="panel-display boxton clearfix radix-boxton" id="mini-panel-oa_toolbar_modern_panel">
                                            <div class="container-fluid">
                                                <div class="row">
                                                    <div class="col-md-12 radix-layouts-content panel-panel">
                                                        <div class="panel-panel-inner">
                                                            <div class="panel-pane pane-oa-responsive-regions-mobile pull-left">
                                                                <div class="pane-content">
                                                                    <div id='oa-mobile-menu' class='oa-responsive-regions-mobile menu sm'>
                                                                        <button type="button" data-toggle="collapse" data-target="#oa-navbar-menu" class="oa-mobile-icon btn btn-navbar navbar-toggle menu ">
                                                                            <span class="sr-only">Toggle menu navigation</span>
                                                                            <span class="fa fa-bars"></span>
                                                                        </button>
                                                                        <div id="oa-navbar-menu" class="collapse">
                                                                            <div class="oa-navbar-inner"></div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div class="panel-pane pane-oa-navigation pull-left menu-mobile-menu">
                                                                <div class="pane-content">
                                                                    <div class="oa-navigation">
                                                                        <nav class="main-menu pull-left" role="navigation">
                                                                            <ul class="menu nav navbar-nav">
                                                                                <li class="first leaf dhtml-menu menu-link-stevensedu" id="dhtml_menu-9581-1">
                                                                                    <a href="http://www.stevens.edu" title="">Stevens.edu</a>
                                                                                </li>
                                                                                <li class="leaf dhtml-menu menu-link-people-finder" id="dhtml_menu-31511-1">
                                                                                    <a href="https://web.stevens.edu/peoplefinder/" title="">People Finder</a>
                                                                                </li>
                                                                                <li class="leaf dhtml-menu menu-link-search" id="dhtml_menu-31516-1">
                                                                                    <a href="/search/site?source=menu" title="">Search</a>
                                                                                </li>
                                                                                <li class="last leaf dhtml-menu menu-link-campus-directory" id="dhtml_menu-31716-1">
                                                                                    <a href="/directory" title="">Campus Directory</a>
                                                                                </li>
                                                                            </ul>
                                                                        </nav>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div class="panel-pane pane-oa-tour-custom-pane pull-right oa-mobile-icon">
                                                                <div class="pane-content">
                                                                    <ul class="oa-tours">
                                                                        <li class="dropdown  align-right btn-group">
                                                                            <a class="dropdown-toggle btn  btn-inverse" id="tours-dropdown" data-toggle="dropdown" href="#" title="Site Tours">
                                                                                <i class="icon-question-sign"></i>
                                                                                <span class="element-invisible">Site Tours</span>
                                                                            </a>
                                                                            <ul class="dropdown-menu" role="menu" aria-labelledby="space-dropdown">
                                                                                <li class="dropdown-column">
                                                                                    <div class="item-list">
                                                                                        <ul>
                                                                                            <li class="first">
                                                                                                <a href="/?tour=mystevens_search" class="active">myStevens 2.0 - Search</a>
                                                                                            </li>
                                                                                            <li>
                                                                                                <a href="/?tour=mystevens_2_0_events" class="active">myStevens 2.0 - Events</a>
                                                                                            </li>
                                                                                            <li>
                                                                                                <a href="/?tour=mystevens_2_0_help" class="active">myStevens 2.0 - Help</a>
                                                                                            </li>
                                                                                            <li>
                                                                                                <a href="/?tour=mystevens_2_0_directory" class="active">myStevens 2.0 - Directory</a>
                                                                                            </li>
                                                                                            <li>
                                                                                                <a href="/?tour=mystevens_2_0_my_info" class="active">myStevens 2.0 - My Info</a>
                                                                                            </li>
                                                                                            <li>
                                                                                                <a href="/?tour=mystevens_2_0_alerts" class="active">myStevens 2.0 - Alerts</a>
                                                                                            </li>
                                                                                            <li>
                                                                                                <a href="/?tour=mystevens_2_0_feedback" class="active">myStevens 2.0 - Feedback</a>
                                                                                            </li>
                                                                                            <li class="last">
                                                                                                <a href="/?tour=mystevens_2_0_custom_bookmarks" class="active">myStevens 2.0 - Custom Bookmarks</a>
                                                                                            </li>
                                                                                        </ul>
                                                                                    </div>
                                                                                </li>
                                                                            </ul>
                                                                        </li>
                                                                    </ul>
                                                                </div>
                                                            </div>
                                                            <div class="panel-pane pane-block pane-oa-toolbar-oa-user-badge pull-right">
                                                                <div class="pane-content">
                                                                    <div id="oa-user-badge">
                                                                        <div class="dropdown oa-dropdown btn-group">
                                                                            <div class="dropdown-toggle btn clearfix user-badge btn-inverse" id="user-badge-dropdown" data-toggle="dropdown">
                                                                                <span>Marcus Simpkins</span>
                                                                                <img src="https://my.stevens.edu/profiles/openatrium/modules/contrib/oa_core/modules/oa_users/oa-user.png" width="30" height="30" alt="Your profile picture"/>
                                                                            </div>
                                                                            <div class="dropdown-menu dropdown-menu-right" role="menu" aria-labelledby="section-dropdown">
                                                                                <ul class="links">
                                                                                    <li class="dashboard first">
                                                                                        <a href="/user/124926/view">My Info</a>
                                                                                    </li>
                                                                                    <li class="logout last">
                                                                                        <a href="/user/logout">Log out</a>
                                                                                    </li>
                                                                                </ul>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div class="panel-pane pane-oa-toolbar-search search-mobile-menu pull-right">
                                                                <div class="pane-content">
                                                                    <div class="toolbar-search">
                                                                        <form action="search/site" method="post">
                                                                            <div class="input-append">
                                                                                <input type="text" class="search-text form-control" name="search_text">
                                                                                <div class="btn-group dropdown">
                                                                                    <button type="submit" class="btn submit btn-inverse">
                                                                                        <i class="icon-search"></i>
                                                                                        <span class="element-invisible">Search Button</span>
                                                                                    </button>
                                                                                    <a class="btn dropdown-toggle btn-inverse" data-toggle="dropdown">
                                                                                        <i class="caret"></i>
                                                                                        <span class="element-invisible">Search Options</span>
                                                                                    </a>
                                                                                    <ul class="dropdown-menu options radio">
                                                                                        <li>
                                                                                            <label class="radio">
                                                                                                <input type="radio" name="searchOptions" value="all_spaces" checked>All spaces            
                                                                                            </label>
                                                                                        </li>
                                                                                        <li>
                                                                                            <label class="radio">
                                                                                                <input type="radio" name="searchOptions" value="this_space">This space            
                                                                                            </label>
                                                                                        </li>
                                                                                        <li>
                                                                                            <label class="radio">
                                                                                                <input type="radio" name="searchOptions" value="users">Users            
                                                                                            </label>
                                                                                        </li>
                                                                                    </ul>
                                                                                </div>
                                                                            </div>
                                                                        </form>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div class="panel-pane pane-oa-responsive-regions-mobile pull-right">
                                                                <div class="pane-content">
                                                                    <div id='oa-mobile-search' class='oa-responsive-regions-mobile search sm'>
                                                                        <button type="button" data-toggle="collapse" data-target="#oa-navbar-search" class="oa-mobile-icon btn btn-navbar navbar-toggle search ">
                                                                            <span class="sr-only">Toggle search navigation</span>
                                                                            <span class="fa fa-search"></span>
                                                                        </button>
                                                                        <div id="oa-navbar-search" class="collapse">
                                                                            <div class="oa-navbar-inner"></div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <!-- /.boxton -->
                                    </div>
                                </div>
                            </div>
                        </div>
                    </header>
                </div>
                <div class="row oa-flex-grow">
                    <div class="col-md-3 oa-layout-sidebar1 panel-panel pull-left">
                        <div class="panel-panel-inner">
                            <div class="oa-responsive-region oa-responsive-desktop oa-responsive-region-left oa-responsive-fixed " data-position="left">
                                <div class="oa-responsive-region-inner">
                                    <div class="panel-pane pane-panels-mini pane-oa-admin-minipanel">
                                        <div class="pane-content">
                                            <div class="panel-display boxton clearfix radix-boxton" id="mini-panel-oa_admin_minipanel">
                                                <div class="container-fluid">
                                                    <div class="row">
                                                        <div class="col-md-12 radix-layouts-content panel-panel">
                                                            <div class="panel-panel-inner">
                                                                <div class="panel-pane pane-oa-space-structure">
                                                                    <div class="pane-content">
                                                                        <ul class="oa-space-structure oa_toolbar">
                                                                            <li class="dropdown btn-group">
                                                                                <a href="#" class="dropdown-toggle btn btn-circle btn-inverse" title="Space Structure" data-toggle="dropdown">
                                                                                    <i class="fa fa-sitemap"></i>
                                                                                    <span class='element-invisible'>Space Structure</span>
                                                                                </a>
                                                                                <ul class="dropdown-menu oa-noscroll" id="oa-space-menu" role="menu">
                                                                                    <li>
                                                                                        <div class="item-list">
                                                                                            <h3>
                                                                                                <a href="/mystevens-portal">myStevens Portal</a>
                                                                                            </h3>
                                                                                            <ul>
                                                                                                <li class="first">
                                                                                                    <a href="/sitemap">Site map</a>
                                                                                                </li>
                                                                                                <li>
                                                                                                    <a href="/spaces">All Spaces...</a>
                                                                                                </li>
                                                                                                <li class="last">
                                                                                                    <a href="/groups">All Groups...</a>
                                                                                                </li>
                                                                                            </ul>
                                                                                        </div>
                                                                                    </li>
                                                                                </ul>
                                                                            </li>
                                                                        </ul>
                                                                    </div>
                                                                </div>
                                                                <div class="panel-pane pane-oa-members-toolbar">
                                                                    <div class="pane-content">
                                                                        <ul class="oa-members-toolbar oa_toolbar">
                                                                            <li class='dropdown btn-group'>
                                                                                <a href="#" class="dropdown-toggle btn btn-circle " data-toggle='dropdown' title="Space Members">
                                                                                    <i class="icon-user"></i>
                                                                                    <span class="element-invisible">Space Members</span>
                                                                                </a>
                                                                                <ul class="dropdown-menu" role="menu">
                                                                                    <li class="dropdown-column">
                                                                                        <div class="item-list">
                                                                                            <h3>myStevens Portal</h3>
                                                                                            <h4 class="oa-border-top">Admins</h4>
                                                                                            <ul class="links">
                                                                                                <li class="16 first">
                                                                                                    <a href="/users/timothy-m-bridge">tbridge</a>
                                                                                                </li>
                                                                                                <li class="11 last">
                                                                                                    <a href="/users/michael-g-forbes">mforbes</a>
                                                                                                </li>
                                                                                            </ul>
                                                                                            <h4 class="oa-border-top">Members</h4>
                                                                                            <h5>No members</h5>
                                                                                        </div>
                                                                                    </li>
                                                                                </ul>
                                                                            </li>
                                                                        </ul>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <!-- /.boxton -->
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <main id="main-wrapper" class="panel-panel oa-layout-fluid">
                        <div id="main" class="main container row">
                            <div class="col-md-12 oa-layout-contentheader panel-panel">
                                <div class="panel-panel-inner">
                                    <div class="panel-pane pane-block pane-stevens-mystevens-feedback-feedback-form">
                                        <div class="pane-content">
                                            <div id="feedback-btn" data-toggle="modal" data-target="#myModal">
                                                <p>Feedback</p>
                                            </div>
                                            <div class="alert alert-success text-center" id="thank-you" role="status" aria-live="polite" aria-atomic="true">
                                                <span class="glyphicon glyphicon-ok" aria-hidden="true"></span>
                                                Success:Thank you for your feedback
                                            </div>
                                            <div class="alert alert-danger text-center" id="db-error" role="alert" aria-atomic="true">
                                                <span class="glyphicon glyphicon-exclamation-sign" aria-hidden="true"></span>
                                                Error:Please try again leter
                                            </div>
                                            <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" data-keyboard="true" data-backdrop="static">
                                                <div class="modal-dialog" role="document">
                                                    <div class="col-md-10 modal-content">
                                                        <form role="form" class="form-horizontal" id="form" data-toggle="validator">
                                                            <div id="feedback" class="modal-header">
                                                                <button type="button" class="close reset" data-dismiss="modal" aria-label="Close">
                                                                    <span aria-hidden="true">&times;</span>
                                                                </button>
                                                                <h4 class="modal-title text-center" id="myModalLabel">Submit Feedback!</h4>
                                                                <br>
                                                                <p>*We would like to get your feedback on how myStevens should be improved. Tell us about new features we should consider or how we can improve existing features.</p>
                                                            </div>
                                                            <div class="modal-body well well-sm">
                                                                <div class="form-group">
                                                                    <label for="inputEmail" class="col-md-3 control-label">
                                                                        Email <span style="color:red">*</span>
                                                                    </label>
                                                                    <div class="col-md-8">
                                                                        <input type="text" class="form-control" id="inputEmail" disabled value="msimpkin@stevens.edu">
                                                                    </div>
                                                                </div>
                                                                <div class="form-group">
                                                                    <label for="comment" class="col-md-3 control-label">
                                                                        Comment <span style="color:red">*</span>
                                                                    </label>
                                                                    <div class="col-md-8">
                                                                        <textarea class="form-control" rows="3" id="comment"></textarea>
                                                                        <p id="textbox-error" class="error" style="display:none" role="alert" aria-atomic="true">
                                                                            <span class="glyphicon glyphicon-exclamation-sign" aria-hidden="true"></span>
                                                                            Comment cannot be empty.   
                                                                        </p>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div class="modal-footer">
                                                                <div class="feedback-inline">
                                                                    <button type="button" class="btn btn-default reset" data-dismiss="modal">Close</button>
                                                                </div>
                                                                <div class="feedback-inline">
                                                                    <button type="submit" id="submit-button" class="btn btn-primary">Submit</button>
                                                                </div>
                                                            </div>
                                                        </form>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <a id="main-content"></a>
                            <div class="col-md-12 oa-layout-content content panel-panel">
                                <div class="panel-panel-inner">
                                    <div class="oa-horizontal-slice style-region">
                                        <div class="panel-pane pane-page-content">
                                            <div class="pane-content">
                                                <div class="panel-display selby clearfix radix-selby" id="page-page">
                                                    <div class="container-fluid">
                                                        <div class="row">
                                                            <div class="col-md-4 radix-layouts-sidebar panel-panel">
                                                                <div class="panel-panel-inner">
                                                                    <section class="mystevens-pane  ">
                                                                        <div class="mystevens-pane-title large-header">
                                                                            <h2>Bookmarks      </h2>
                                                                        </div>
                                                                        <div class="arrow-down large-arrow"></div>
                                                                        <div class="mystevens-pane-content clearfix large-pane gray-bg">
                                                                            <div class="view view-mystevens view-id-mystevens view-display-id-panel_pane_7 mystevens-icon-fluid-grid view-dom-id-d0b7e398247f4a868c95d9e893aa95b6">
                                                                                <div class="view-content">
                                                                                    <div class="item-list">
                                                                                        <ul>
                                                                                            <li class="views-row views-row-1 views-row-odd views-row-first">
                                                                                                <div class="views-field views-field-uuid">
                                                                                                    <span class="field-content">
                                                                                                        <div class="badge portal-badge" id="badge-10d04878-e399-4131-ade2-48aad8b6917f"></div>
                                                                                                    </span>
                                                                                                </div>
                                                                                                <div class="views-field views-field-field-icon">
                                                                                                    <div class="field-content">
                                                                                                        <a href="https://webmail.stevens.edu" target="_blank">
                                                                                                            <img class="campus-service-icon" src="https://my.stevens.edu/sites/default/files/styles/campus_service_icon/public/owa.png?itok=KbSKSVqe" width="51" height="52" alt=""/>
                                                                                                        </a>
                                                                                                    </div>
                                                                                                </div>
                                                                                                <div class="views-field views-field-title">
                                                                                                    <span class="field-content">
                                                                                                        <a href="https://webmail.stevens.edu" target="_blank">Outlook Web App</a>
                                                                                                    </span>
                                                                                                </div>
                                                                                            </li>
                                                                                            <li class="views-row views-row-2 views-row-even">
                                                                                                <div class="views-field views-field-uuid">
                                                                                                    <span class="field-content">
                                                                                                        <div class="badge portal-badge" id="badge-43745184-2cfa-49b8-9486-9efdd256290f"></div>
                                                                                                    </span>
                                                                                                </div>
                                                                                                <div class="views-field views-field-field-icon">
                                                                                                    <div class="field-content">
                                                                                                        <a href="https://outlook.office365.com/owa/?path=/calendar" target="_blank">
                                                                                                            <img class="campus-service-icon" src="https://my.stevens.edu/sites/default/files/styles/campus_service_icon/public/mystevens_icons/outlook_cal_52.png?itok=Ag2yWUdq" width="57" height="52" alt=""/>
                                                                                                        </a>
                                                                                                    </div>
                                                                                                </div>
                                                                                                <div class="views-field views-field-title">
                                                                                                    <span class="field-content">
                                                                                                        <a href="https://outlook.office365.com/owa/?path=/calendar" target="_blank">Outlook Calendar</a>
                                                                                                    </span>
                                                                                                </div>
                                                                                            </li>
                                                                                            <li class="views-row views-row-3 views-row-odd">
                                                                                                <div class="views-field views-field-uuid">
                                                                                                    <span class="field-content">
                                                                                                        <div class="badge portal-badge" id="badge-d30d2b53-dbc1-41a1-86e2-b844232979cd"></div>
                                                                                                    </span>
                                                                                                </div>
                                                                                                <div class="views-field views-field-field-icon">
                                                                                                    <div class="field-content">
                                                                                                        <a href="https://wd5.myworkday.com/stevens" target="_blank">
                                                                                                            <img class="campus-service-icon" src="https://my.stevens.edu/sites/default/files/styles/campus_service_icon/public/workday.png?itok=BX7pSB3E" width="46" height="52" alt=""/>
                                                                                                        </a>
                                                                                                    </div>
                                                                                                </div>
                                                                                                <div class="views-field views-field-title">
                                                                                                    <span class="field-content">
                                                                                                        <a href="https://wd5.myworkday.com/stevens" target="_blank">Workday</a>
                                                                                                    </span>
                                                                                                </div>
                                                                                            </li>
                                                                                            <li class="views-row views-row-4 views-row-even">
                                                                                                <div class="views-field views-field-uuid">
                                                                                                    <span class="field-content">
                                                                                                        <div class="badge portal-badge" id="badge-7c62b5bd-8404-49db-a8af-914a92af5fe3"></div>
                                                                                                    </span>
                                                                                                </div>
                                                                                                <div class="views-field views-field-field-icon">
                                                                                                    <div class="field-content">
                                                                                                        <a href="http://www.stevens.edu/canvas" target="_blank">
                                                                                                            <img class="campus-service-icon" src="https://my.stevens.edu/sites/default/files/styles/campus_service_icon/public/canvas.png?itok=dcBS83ef" width="52" height="52" alt=""/>
                                                                                                        </a>
                                                                                                    </div>
                                                                                                </div>
                                                                                                <div class="views-field views-field-title">
                                                                                                    <span class="field-content">
                                                                                                        <a href="http://www.stevens.edu/canvas" target="_blank">Canvas</a>
                                                                                                    </span>
                                                                                                </div>
                                                                                            </li>
                                                                                            <li class="views-row views-row-5 views-row-odd">
                                                                                                <div class="views-field views-field-uuid">
                                                                                                    <span class="field-content">
                                                                                                        <div class="badge portal-badge" id="badge-61d9de39-799d-4c47-9bab-8a9fb53d5cc0"></div>
                                                                                                    </span>
                                                                                                </div>
                                                                                                <div class="views-field views-field-field-icon">
                                                                                                    <div class="field-content">
                                                                                                        <a href="http://sit.teamdynamix.com/TDClient/Home/" target="_blank">
                                                                                                            <img class="campus-service-icon" src="https://my.stevens.edu/sites/default/files/styles/campus_service_icon/public/td.png?itok=6HsUyAEc" width="52" height="52" alt=""/>
                                                                                                        </a>
                                                                                                    </div>
                                                                                                </div>
                                                                                                <div class="views-field views-field-title">
                                                                                                    <span class="field-content">
                                                                                                        <a href="http://sit.teamdynamix.com/TDClient/Home/" target="_blank">IT Service Desk</a>
                                                                                                    </span>
                                                                                                </div>
                                                                                            </li>
                                                                                            <li class="views-row views-row-6 views-row-even">
                                                                                                <div class="views-field views-field-uuid">
                                                                                                    <span class="field-content">
                                                                                                        <div class="badge portal-badge" id="badge-7e8c48d8-9d25-4962-b310-4391b968e6ee"></div>
                                                                                                    </span>
                                                                                                </div>
                                                                                                <div class="views-field views-field-field-icon">
                                                                                                    <div class="field-content">
                                                                                                        <a href="https://mystevens.stevens.edu/sso/webselfservices.php" target="_blank">
                                                                                                            <img class="campus-service-icon" src="https://my.stevens.edu/sites/default/files/styles/campus_service_icon/public/webself.png?itok=7ukoFyCP" width="65" height="52" alt=""/>
                                                                                                        </a>
                                                                                                    </div>
                                                                                                </div>
                                                                                                <div class="views-field views-field-title">
                                                                                                    <span class="field-content">
                                                                                                        <a href="https://mystevens.stevens.edu/sso/webselfservices.php" target="_blank">Student/Faculty Web Self Services</a>
                                                                                                    </span>
                                                                                                </div>
                                                                                            </li>
                                                                                            <li class="views-row views-row-7 views-row-odd">
                                                                                                <div class="views-field views-field-uuid">
                                                                                                    <span class="field-content">
                                                                                                        <div class="badge portal-badge" id="badge-4dbf874a-c40e-4815-9489-645b12d3ca91"></div>
                                                                                                    </span>
                                                                                                </div>
                                                                                                <div class="views-field views-field-field-icon">
                                                                                                    <div class="field-content">
                                                                                                        <a href="https://www.stevens.edu/studentebilling" target="_blank">
                                                                                                            <img class="campus-service-icon" src="https://my.stevens.edu/sites/default/files/styles/campus_service_icon/public/ebilling.png?itok=QWZAv1i8" width="69" height="52" alt=""/>
                                                                                                        </a>
                                                                                                    </div>
                                                                                                </div>
                                                                                                <div class="views-field views-field-title">
                                                                                                    <span class="field-content">
                                                                                                        <a href="https://www.stevens.edu/studentebilling" target="_blank">eBilling</a>
                                                                                                    </span>
                                                                                                </div>
                                                                                            </li>
                                                                                            <li class="views-row views-row-8 views-row-even">
                                                                                                <div class="views-field views-field-uuid">
                                                                                                    <span class="field-content">
                                                                                                        <div class="badge portal-badge" id="badge-a0699c23-3dfd-4f56-a3f3-1ff718e216e7"></div>
                                                                                                    </span>
                                                                                                </div>
                                                                                                <div class="views-field views-field-field-icon">
                                                                                                    <div class="field-content">
                                                                                                        <a href="https://my.stevens.edu/it/content/staying-safe-online" target="_blank">
                                                                                                            <img class="campus-service-icon" src="https://my.stevens.edu/sites/default/files/styles/campus_service_icon/public/mystevens_icons/2000px-lock_font_awesome.svg_.png?itok=yyQroS5b" width="52" height="52" alt="Staying Safe Online" title="Staying Safe Online"/>
                                                                                                        </a>
                                                                                                    </div>
                                                                                                </div>
                                                                                                <div class="views-field views-field-title">
                                                                                                    <span class="field-content">
                                                                                                        <a href="https://my.stevens.edu/it/content/staying-safe-online" target="_blank">Staying Safe Online</a>
                                                                                                    </span>
                                                                                                </div>
                                                                                            </li>
                                                                                            <li class="views-row views-row-9 views-row-odd">
                                                                                                <div class="views-field views-field-uuid">
                                                                                                    <span class="field-content">
                                                                                                        <div class="badge portal-badge" id="badge-76d03ea7-ccda-45ef-8eb5-b0f03c76c50d"></div>
                                                                                                    </span>
                                                                                                </div>
                                                                                                <div class="views-field views-field-field-icon">
                                                                                                    <div class="field-content">
                                                                                                        <a href="https://my.stevens.edu/campus-card-office" target="_blank">
                                                                                                            <img class="campus-service-icon" src="https://my.stevens.edu/sites/default/files/styles/campus_service_icon/public/mystevens_icons/duckcard.jpg_1.jpg?itok=w_sFBVQk" width="34" height="52" alt=""/>
                                                                                                        </a>
                                                                                                    </div>
                                                                                                </div>
                                                                                                <div class="views-field views-field-title">
                                                                                                    <span class="field-content">
                                                                                                        <a href="https://my.stevens.edu/campus-card-office" target="_blank">DuckCard Office (DuckBills)</a>
                                                                                                    </span>
                                                                                                </div>
                                                                                            </li>
                                                                                            <li class="views-row views-row-10 views-row-even">
                                                                                                <div class="views-field views-field-uuid">
                                                                                                    <span class="field-content">
                                                                                                        <div class="badge portal-badge" id="badge-a729ecbb-d537-4048-8167-e615e20851e0"></div>
                                                                                                    </span>
                                                                                                </div>
                                                                                                <div class="views-field views-field-field-icon">
                                                                                                    <div class="field-content">
                                                                                                        <a href="https://ra.vdi.stevens.edu/" target="_blank">
                                                                                                            <img class="campus-service-icon" src="https://my.stevens.edu/sites/default/files/styles/campus_service_icon/public/mystevens_icons/vle.png?itok=LOsTTmJo" width="83" height="52" alt=""/>
                                                                                                        </a>
                                                                                                    </div>
                                                                                                </div>
                                                                                                <div class="views-field views-field-title">
                                                                                                    <span class="field-content">
                                                                                                        <a href="https://ra.vdi.stevens.edu/" target="_blank">Virtual Learning Environment</a>
                                                                                                    </span>
                                                                                                </div>
                                                                                            </li>
                                                                                            <li class="views-row views-row-11 views-row-odd">
                                                                                                <div class="views-field views-field-uuid">
                                                                                                    <span class="field-content">
                                                                                                        <div class="badge portal-badge" id="badge-799b7ac4-28e7-49b2-83ec-44d849c8a6f1"></div>
                                                                                                    </span>
                                                                                                </div>
                                                                                                <div class="views-field views-field-field-icon">
                                                                                                    <div class="field-content">
                                                                                                        <a href="https://www.stevens.edu/workorder" target="_blank">
                                                                                                            <img class="campus-service-icon" src="https://my.stevens.edu/sites/default/files/styles/campus_service_icon/public/workorder.png?itok=0ZS0EJ25" width="51" height="52" alt=""/>
                                                                                                        </a>
                                                                                                    </div>
                                                                                                </div>
                                                                                                <div class="views-field views-field-title">
                                                                                                    <span class="field-content">
                                                                                                        <a href="https://www.stevens.edu/workorder" target="_blank">Facilities Work Order</a>
                                                                                                    </span>
                                                                                                </div>
                                                                                            </li>
                                                                                            <li class="views-row views-row-12 views-row-even">
                                                                                                <div class="views-field views-field-uuid">
                                                                                                    <span class="field-content">
                                                                                                        <div class="badge portal-badge" id="badge-b92c9fe9-f939-4272-997c-207787faef0b"></div>
                                                                                                    </span>
                                                                                                </div>
                                                                                                <div class="views-field views-field-field-icon">
                                                                                                    <div class="field-content">
                                                                                                        <a href="https://mystevens.stevens.edu/housingApplicationLogin.php" target="_blank">
                                                                                                            <img class="campus-service-icon" src="https://my.stevens.edu/sites/default/files/styles/campus_service_icon/public/housing.png?itok=6_2hY6iw" width="64" height="52" alt=""/>
                                                                                                        </a>
                                                                                                    </div>
                                                                                                </div>
                                                                                                <div class="views-field views-field-title">
                                                                                                    <span class="field-content">
                                                                                                        <a href="https://mystevens.stevens.edu/housingApplicationLogin.php" target="_blank">Housing &amp;Dining</a>
                                                                                                    </span>
                                                                                                </div>
                                                                                            </li>
                                                                                            <li class="views-row views-row-13 views-row-odd">
                                                                                                <div class="views-field views-field-uuid">
                                                                                                    <span class="field-content">
                                                                                                        <div class="badge portal-badge" id="badge-f7a1d533-6aee-4f93-966a-5bea0e854a55"></div>
                                                                                                    </span>
                                                                                                </div>
                                                                                                <div class="views-field views-field-field-icon">
                                                                                                    <div class="field-content">
                                                                                                        <a href="https://www.stevens.edu/report" target="_blank">
                                                                                                            <img class="campus-service-icon" src="https://my.stevens.edu/sites/default/files/styles/campus_service_icon/public/mystevens_icons/incident_care_report.png?itok=ZqUWU9x1" width="63" height="52" alt=""/>
                                                                                                        </a>
                                                                                                    </div>
                                                                                                </div>
                                                                                                <div class="views-field views-field-title">
                                                                                                    <span class="field-content">
                                                                                                        <a href="https://www.stevens.edu/report" target="_blank">Report a Concern</a>
                                                                                                    </span>
                                                                                                </div>
                                                                                            </li>
                                                                                            <li class="views-row views-row-14 views-row-even">
                                                                                                <div class="views-field views-field-uuid">
                                                                                                    <span class="field-content">
                                                                                                        <div class="badge portal-badge" id="badge-609278b1-a56a-4621-97bf-45a88e497b8f"></div>
                                                                                                    </span>
                                                                                                </div>
                                                                                                <div class="views-field views-field-field-icon">
                                                                                                    <div class="field-content">
                                                                                                        <a href="http://stevens.edu/alerts" target="_blank">
                                                                                                            <img class="campus-service-icon" src="https://my.stevens.edu/sites/default/files/styles/campus_service_icon/public/mystevens_icons/everbridge_logo.png?itok=zHHYqDQ7" width="73" height="52"/>
                                                                                                        </a>
                                                                                                    </div>
                                                                                                </div>
                                                                                                <div class="views-field views-field-title">
                                                                                                    <span class="field-content">
                                                                                                        <a href="http://stevens.edu/alerts" target="_blank">Alerts</a>
                                                                                                    </span>
                                                                                                </div>
                                                                                            </li>
                                                                                            <li class="views-row views-row-15 views-row-odd">
                                                                                                <div class="views-field views-field-uuid">
                                                                                                    <span class="field-content">
                                                                                                        <div class="badge portal-badge" id="badge-61132cb4-6ce2-4745-8c41-c18bb02bff8a"></div>
                                                                                                    </span>
                                                                                                </div>
                                                                                                <div class="views-field views-field-field-icon">
                                                                                                    <div class="field-content">
                                                                                                        <a href="https://web.stevens.edu/peoplefinder/" target="_blank">
                                                                                                            <img class="campus-service-icon" src="https://my.stevens.edu/sites/default/files/styles/campus_service_icon/public/mystevens_icons/peoplefinder.png?itok=eHHy3LWx" width="51" height="52"/>
                                                                                                        </a>
                                                                                                    </div>
                                                                                                </div>
                                                                                                <div class="views-field views-field-title">
                                                                                                    <span class="field-content">
                                                                                                        <a href="https://web.stevens.edu/peoplefinder/" target="_blank">People Finder</a>
                                                                                                    </span>
                                                                                                </div>
                                                                                            </li>
                                                                                            <li class="views-row views-row-16 views-row-even">
                                                                                                <div class="views-field views-field-uuid">
                                                                                                    <span class="field-content">
                                                                                                        <div class="badge portal-badge" id="badge-62b4a3ca-602b-413b-a7f2-19f28a0d34e1"></div>
                                                                                                    </span>
                                                                                                </div>
                                                                                                <div class="views-field views-field-field-icon">
                                                                                                    <div class="field-content">
                                                                                                        <a href="https://portal.office.com/" target="_blank">
                                                                                                            <img class="campus-service-icon" src="https://my.stevens.edu/sites/default/files/styles/campus_service_icon/public/mystevens_icons/o365_trans_1.png?itok=uWenkslN" width="44" height="52" alt="Office 365 Logo" title="Office 365"/>
                                                                                                        </a>
                                                                                                    </div>
                                                                                                </div>
                                                                                                <div class="views-field views-field-title">
                                                                                                    <span class="field-content">
                                                                                                        <a href="https://portal.office.com/" target="_blank">Office 365 Apps</a>
                                                                                                    </span>
                                                                                                </div>
                                                                                            </li>
                                                                                            <li class="views-row views-row-17 views-row-odd">
                                                                                                <div class="views-field views-field-uuid">
                                                                                                    <span class="field-content">
                                                                                                        <div class="badge portal-badge" id="badge-766d26eb-8911-45f9-b945-2e9adb4c729a"></div>
                                                                                                    </span>
                                                                                                </div>
                                                                                                <div class="views-field views-field-field-icon">
                                                                                                    <div class="field-content">
                                                                                                        <a href="https://drive.google.com/a/stevens.edu" target="_blank">
                                                                                                            <img class="campus-service-icon" src="https://my.stevens.edu/sites/default/files/styles/campus_service_icon/public/drive.png?itok=plL4cdpK" width="52" height="52" alt=""/>
                                                                                                        </a>
                                                                                                    </div>
                                                                                                </div>
                                                                                                <div class="views-field views-field-title">
                                                                                                    <span class="field-content">
                                                                                                        <a href="https://drive.google.com/a/stevens.edu" target="_blank">Google Drive</a>
                                                                                                    </span>
                                                                                                </div>
                                                                                            </li>
                                                                                            <li class="views-row views-row-18 views-row-even">
                                                                                                <div class="views-field views-field-uuid">
                                                                                                    <span class="field-content">
                                                                                                        <div class="badge portal-badge" id="badge-1d292bf3-294d-492e-9791-cee291bed8d9"></div>
                                                                                                    </span>
                                                                                                </div>
                                                                                                <div class="views-field views-field-field-icon">
                                                                                                    <div class="field-content">
                                                                                                        <a href="https://www.google.com/calendar/hosted/stevens.edu" target="_blank">
                                                                                                            <img class="campus-service-icon" src="https://my.stevens.edu/sites/default/files/styles/campus_service_icon/public/calendar.png?itok=XwlGCqdN" width="52" height="52" alt=""/>
                                                                                                        </a>
                                                                                                    </div>
                                                                                                </div>
                                                                                                <div class="views-field views-field-title">
                                                                                                    <span class="field-content">
                                                                                                        <a href="https://www.google.com/calendar/hosted/stevens.edu" target="_blank">Google Calendar</a>
                                                                                                    </span>
                                                                                                </div>
                                                                                            </li>
                                                                                            <li class="views-row views-row-19 views-row-odd">
                                                                                                <div class="views-field views-field-uuid">
                                                                                                    <span class="field-content">
                                                                                                        <div class="badge portal-badge" id="badge-f75ac0d5-9ee7-4810-a991-ab5fcf201245"></div>
                                                                                                    </span>
                                                                                                </div>
                                                                                                <div class="views-field views-field-field-icon">
                                                                                                    <div class="field-content">
                                                                                                        <a href="https://stevens.joinhandshake.com/login" target="_blank">
                                                                                                            <img class="campus-service-icon" src="https://my.stevens.edu/sites/default/files/styles/campus_service_icon/public/mystevens_icons/logo-icon-0bca123d4668f6fc56c65f8ae580c718bcdc45f8109d3e0bb6f1fded9584aaf4.png?itok=HCAEE99J" width="52" height="52" alt=""/>
                                                                                                        </a>
                                                                                                    </div>
                                                                                                </div>
                                                                                                <div class="views-field views-field-title">
                                                                                                    <span class="field-content">
                                                                                                        <a href="https://stevens.joinhandshake.com/login" target="_blank">Handshake</a>
                                                                                                    </span>
                                                                                                </div>
                                                                                            </li>
                                                                                            <li class="views-row views-row-20 views-row-even">
                                                                                                <div class="views-field views-field-uuid">
                                                                                                    <span class="field-content">
                                                                                                        <div class="badge portal-badge" id="badge-33b0caf0-da4a-41de-a4ea-79d197751ad4"></div>
                                                                                                    </span>
                                                                                                </div>
                                                                                                <div class="views-field views-field-field-icon">
                                                                                                    <div class="field-content">
                                                                                                        <a href="https://www.stevens.edu/lynda" target="_blank">
                                                                                                            <img class="campus-service-icon" src="https://my.stevens.edu/sites/default/files/styles/campus_service_icon/public/mystevens_icons/lynda.png?itok=YmvlaLr7" width="52" height="52" alt=""/>
                                                                                                        </a>
                                                                                                    </div>
                                                                                                </div>
                                                                                                <div class="views-field views-field-title">
                                                                                                    <span class="field-content">
                                                                                                        <a href="https://www.stevens.edu/lynda" target="_blank">Lynda</a>
                                                                                                    </span>
                                                                                                </div>
                                                                                            </li>
                                                                                            <li class="views-row views-row-21 views-row-odd views-row-last">
                                                                                                <div class="views-field views-field-uuid">
                                                                                                    <span class="field-content">
                                                                                                        <div class="badge portal-badge" id="badge-89608872-e56c-48cb-9b5c-7fdd35ad4b6d"></div>
                                                                                                    </span>
                                                                                                </div>
                                                                                                <div class="views-field views-field-field-icon">
                                                                                                    <div class="field-content">
                                                                                                        <a href="https://www.stevens.edu/password" target="_blank">
                                                                                                            <img class="campus-service-icon" src="https://my.stevens.edu/sites/default/files/styles/campus_service_icon/public/mystevens_icons/1469494962_password.png?itok=utSut24L" width="52" height="52" alt=""/>
                                                                                                        </a>
                                                                                                    </div>
                                                                                                </div>
                                                                                                <div class="views-field views-field-title">
                                                                                                    <span class="field-content">
                                                                                                        <a href="https://www.stevens.edu/password" target="_blank">Password Service</a>
                                                                                                    </span>
                                                                                                </div>
                                                                                            </li>
                                                                                        </ul>
                                                                                    </div>
                                                                                </div>
                                                                                <div class="view-footer">
                                                                                    <div id="manage-bookmark-actions" class="pull-right">
                                                                                        <a id="manage-bookmarks-add" class="manage-bookmarks-link" href="/node/add/bookmark?destination=/">
                                                                                            <img id="manage-bookmarks-add-img" class="manage-bookmarks-action-img" width="20px" src="/sites/default/themes/stevens_contempo/assets/images/icon/icon-plus.png "/>
                                                                                        </a>
                                                                                        <a id="manage-bookmarks-edit" class="manage-bookmarks-link" href="/portal/manage-bookmarks">
                                                                                            <img id="manage-bookmarks-edit-img" class="manage-bookmarks-action-img" width="20px" src="/sites/default/themes/stevens_contempo/assets/images/icon/icon-gear.png "/>
                                                                                        </a>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </section>
                                                                    <section class="mystevens-pane  ">
                                                                        <div class="mystevens-pane-content clearfix large-pane gray-bg">
                                                                            <div class="view view-mystevens view-id-mystevens view-display-id-panel_pane_2 view-dom-id-1496a6fa12005bf8aefa743689fccdf6">
                                                                                <div class="view-content">
                                                                                    <div class="item-list">
                                                                                        <ul>
                                                                                            <li class="views-row views-row-1 views-row-odd views-row-first">
                                                                                                <span class="views-field views-field-title">
                                                                                                    <span class="field-content">
                                                                                                        <a href="https://www.stevens.edu/academiccalendar" target="_blank">Academic Calendar</a>
                                                                                                    </span>
                                                                                                </span>
                                                                                                <span class="views-field views-field-field-additional-text">
                                                                                                    <span class="field-content"></span>
                                                                                                </span>
                                                                                            </li>
                                                                                            <li class="views-row views-row-2 views-row-even">
                                                                                                <span class="views-field views-field-title">
                                                                                                    <span class="field-content">
                                                                                                        <a href="https://www.stevens.edu/bookstore" target="_blank">Bookstore</a>
                                                                                                    </span>
                                                                                                </span>
                                                                                                <span class="views-field views-field-field-additional-text">
                                                                                                    <span class="field-content"></span>
                                                                                                </span>
                                                                                            </li>
                                                                                            <li class="views-row views-row-3 views-row-odd">
                                                                                                <span class="views-field views-field-title">
                                                                                                    <span class="field-content">
                                                                                                        <a href="https://www.stevens.edu/assess" target="_blank">Course Surveys</a>
                                                                                                    </span>
                                                                                                </span>
                                                                                                <span class="views-field views-field-field-additional-text">
                                                                                                    <span class="field-content"></span>
                                                                                                </span>
                                                                                            </li>
                                                                                            <li class="views-row views-row-4 views-row-even">
                                                                                                <span class="views-field views-field-title">
                                                                                                    <span class="field-content">
                                                                                                        <a href="http://www.stevens.edu/networkguest" target="_blank">Create Guest Wireless Access</a>
                                                                                                    </span>
                                                                                                </span>
                                                                                                <span class="views-field views-field-field-additional-text">
                                                                                                    <span class="field-content"></span>
                                                                                                </span>
                                                                                            </li>
                                                                                            <li class="views-row views-row-5 views-row-odd">
                                                                                                <span class="views-field views-field-title">
                                                                                                    <span class="field-content">
                                                                                                        <a href="https://www.stevens.edu/stusched/" target="_blank">Download Student Class Schedule</a>
                                                                                                    </span>
                                                                                                </span>
                                                                                                <span class="views-field views-field-field-additional-text">
                                                                                                    <span class="field-content"></span>
                                                                                                </span>
                                                                                            </li>
                                                                                            <li class="views-row views-row-6 views-row-even">
                                                                                                <span class="views-field views-field-title">
                                                                                                    <span class="field-content">
                                                                                                        <a href="https://mail.google.com/a/stevens.edu" target="_blank">Gmail</a>
                                                                                                    </span>
                                                                                                </span>
                                                                                                <span class="views-field views-field-field-additional-text">
                                                                                                    <span class="field-content"></span>
                                                                                                </span>
                                                                                            </li>
                                                                                            <li class="views-row views-row-7 views-row-odd">
                                                                                                <span class="views-field views-field-title">
                                                                                                    <span class="field-content">
                                                                                                        <a href="https://kaltura.stevens.edu" target="_blank">Kaltura</a>
                                                                                                    </span>
                                                                                                </span>
                                                                                                <span class="views-field views-field-field-additional-text">
                                                                                                    <span class="field-content"></span>
                                                                                                </span>
                                                                                            </li>
                                                                                            <li class="views-row views-row-8 views-row-even">
                                                                                                <span class="views-field views-field-title">
                                                                                                    <span class="field-content">
                                                                                                        <a href="http://researchguides.stevens.edu/az.php" target="_blank">Library Databases</a>
                                                                                                    </span>
                                                                                                </span>
                                                                                                <span class="views-field views-field-field-additional-text">
                                                                                                    <span class="field-content"></span>
                                                                                                </span>
                                                                                            </li>
                                                                                            <li class="views-row views-row-9 views-row-odd">
                                                                                                <span class="views-field views-field-title">
                                                                                                    <span class="field-content">
                                                                                                        <a href="https://www.stevens.edu/macreg" target="_blank">MAC Address Registration</a>
                                                                                                    </span>
                                                                                                </span>
                                                                                                <span class="views-field views-field-field-additional-text">
                                                                                                    <span class="field-content"></span>
                                                                                                </span>
                                                                                            </li>
                                                                                            <li class="views-row views-row-10 views-row-even">
                                                                                                <span class="views-field views-field-title">
                                                                                                    <span class="field-content">
                                                                                                        <a href="https://stevens.skyfactor.com/" target="_blank">Mapworks for Undergraduates</a>
                                                                                                    </span>
                                                                                                </span>
                                                                                                <span class="views-field views-field-field-additional-text">
                                                                                                    <span class="field-content"></span>
                                                                                                </span>
                                                                                            </li>
                                                                                            <li class="views-row views-row-11 views-row-odd">
                                                                                                <span class="views-field views-field-title">
                                                                                                    <span class="field-content">
                                                                                                        <a href="https://mymail.stevens.edu/" target="_blank">myMail (archive)</a>
                                                                                                    </span>
                                                                                                </span>
                                                                                                <span class="views-field views-field-field-additional-text">
                                                                                                    <span class="field-content"></span>
                                                                                                </span>
                                                                                            </li>
                                                                                            <li class="views-row views-row-12 views-row-even">
                                                                                                <span class="views-field views-field-title">
                                                                                                    <span class="field-content">
                                                                                                        <a href="https://mystevens.stevens.edu/sso/njtransit.php" target="_blank">NJ Transit Quik-Tik</a>
                                                                                                    </span>
                                                                                                </span>
                                                                                                <span class="views-field views-field-field-additional-text">
                                                                                                    <span class="field-content"></span>
                                                                                                </span>
                                                                                            </li>
                                                                                            <li class="views-row views-row-13 views-row-odd">
                                                                                                <span class="views-field views-field-title">
                                                                                                    <span class="field-content">
                                                                                                        <a href="http://stevens.campuslabs.com/engage" target="_blank">Undergraduate DuckLink</a>
                                                                                                    </span>
                                                                                                </span>
                                                                                                <span class="views-field views-field-field-additional-text">
                                                                                                    <span class="field-content"></span>
                                                                                                </span>
                                                                                            </li>
                                                                                            <li class="views-row views-row-14 views-row-even views-row-last">
                                                                                                <span class="views-field views-field-title">
                                                                                                    <span class="field-content">
                                                                                                        <a href="https://my.stevens.edu/writing-and-communications-center-wcc" target="_blank">Writing and Communications Center</a>
                                                                                                    </span>
                                                                                                </span>
                                                                                                <span class="views-field views-field-field-additional-text">
                                                                                                    <span class="field-content"></span>
                                                                                                </span>
                                                                                            </li>
                                                                                        </ul>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </section>
                                                                </div>
                                                            </div>
                                                            <div class="col-md-8 radix-layouts-content panel-panel">
                                                                <div class="panel-panel-inner">
                                                                    <div class="row">
                                                                        <div class="col-md-12 radix-layouts-contentheader panel-panel">
                                                                            <div class="panel-panel-inner"></div>
                                                                        </div>
                                                                    </div>
                                                                    <div class="row">
                                                                        <div class="col-md-6 radix-layouts-contentcolumn1 panel-panel">
                                                                            <div class="panel-panel-inner">
                                                                                <section class="mystevens-pane  ">
                                                                                    <div class="mystevens-pane-title large-header">
                                                                                        <h2>Upcoming Events      </h2>
                                                                                    </div>
                                                                                    <div class="arrow-down large-arrow"></div>
                                                                                    <div class="mystevens-pane-content clearfix large-pane gray-bg">
                                                                                        <div class="view view-stevens-mystevens-events-by-channel view-id-stevens_mystevens_events_by_channel view-display-id-upcoming_events_small view-dom-id-b3af1a558d0f9b6c50d5d821a9121232">
                                                                                            <div class="view-content">
                                                                                                <div class="item-list">
                                                                                                    <ul>
                                                                                                        <li class="views-row views-row-1 views-row-odd views-row-first">
                                                                                                            <div class="views-field views-field-field-oa-date">
                                                                                                                <div class="field-content">
                                                                                                                    <div class='oa-event-date-wrapper'>
                                                                                                                        <div class='oa-event-date-month-wrapper'>
                                                                                                                            <span class='oa-event-date-month'>Feb    </span>
                                                                                                                        </div>
                                                                                                                        <div class='oa-event-date-day-wrapper'>
                                                                                                                            <span class='oa-event-date-day'>08    </span>
                                                                                                                        </div>
                                                                                                                    </div>
                                                                                                                </div>
                                                                                                            </div>
                                                                                                            <div class="views-field views-field-title">
                                                                                                                <span class="field-content">
                                                                                                                    <a href="https://stevens.campuslabs.com/engage/event/3175042">Chess Club GBM</a>
                                                                                                                </span>
                                                                                                            </div>
                                                                                                            <div class="views-field views-field-field-oa-date-1">
                                                                                                                <div class="field-content">
                                                                                                                    <span class="date-display-single">
                                                                                                                        <div class="date-display-range">
                                                                                                                            <span class="date-display-start">5:00pm</span>
                                                                                                                            to <span class="date-display-end">8:00pm</span>
                                                                                                                        </div>
                                                                                                                    </span>
                                                                                                                </div>
                                                                                                            </div>
                                                                                                            <div class="views-field views-field-field-feed-name">
                                                                                                                <div class="field-content">Undergraduate DuckLink</div>
                                                                                                            </div>
                                                                                                        </li>
                                                                                                        <li class="views-row views-row-2 views-row-even">
                                                                                                            <div class="views-field views-field-field-oa-date">
                                                                                                                <div class="field-content">
                                                                                                                    <div class='oa-event-date-wrapper'>
                                                                                                                        <div class='oa-event-date-month-wrapper'>
                                                                                                                            <span class='oa-event-date-month'>Feb    </span>
                                                                                                                        </div>
                                                                                                                        <div class='oa-event-date-day-wrapper'>
                                                                                                                            <span class='oa-event-date-day'>08    </span>
                                                                                                                        </div>
                                                                                                                    </div>
                                                                                                                </div>
                                                                                                            </div>
                                                                                                            <div class="views-field views-field-title">
                                                                                                                <span class="field-content">
                                                                                                                    <a href="https://stevens.campuslabs.com/engage/event/3145682">AEC Presents: Slow Jam!</a>
                                                                                                                </span>
                                                                                                            </div>
                                                                                                            <div class="views-field views-field-field-oa-date-1">
                                                                                                                <div class="field-content">
                                                                                                                    <span class="date-display-single">
                                                                                                                        <div class="date-display-range">
                                                                                                                            <span class="date-display-start">7:30pm</span>
                                                                                                                            to <span class="date-display-end">9:30pm</span>
                                                                                                                        </div>
                                                                                                                    </span>
                                                                                                                </div>
                                                                                                            </div>
                                                                                                            <div class="views-field views-field-field-feed-name">
                                                                                                                <div class="field-content">Undergraduate DuckLink</div>
                                                                                                            </div>
                                                                                                        </li>
                                                                                                        <li class="views-row views-row-3 views-row-odd">
                                                                                                            <div class="views-field views-field-field-oa-date">
                                                                                                                <div class="field-content">
                                                                                                                    <div class='oa-event-date-wrapper'>
                                                                                                                        <div class='oa-event-date-month-wrapper'>
                                                                                                                            <span class='oa-event-date-month'>Feb    </span>
                                                                                                                        </div>
                                                                                                                        <div class='oa-event-date-day-wrapper'>
                                                                                                                            <span class='oa-event-date-day'>08    </span>
                                                                                                                        </div>
                                                                                                                    </div>
                                                                                                                </div>
                                                                                                            </div>
                                                                                                            <div class="views-field views-field-title">
                                                                                                                <span class="field-content">
                                                                                                                    <a href="https://www.stevens.edu/events/comedy-errors">The Comedy of Errors</a>
                                                                                                                </span>
                                                                                                            </div>
                                                                                                            <div class="views-field views-field-field-oa-date-1">
                                                                                                                <div class="field-content">
                                                                                                                    <span class="date-display-single">8:00pm</span>
                                                                                                                </div>
                                                                                                            </div>
                                                                                                            <div class="views-field views-field-field-feed-name">
                                                                                                                <div class="field-content">Stevens.edu</div>
                                                                                                            </div>
                                                                                                        </li>
                                                                                                        <li class="views-row views-row-4 views-row-even">
                                                                                                            <div class="views-field views-field-field-oa-date">
                                                                                                                <div class="field-content">
                                                                                                                    <div class='oa-event-date-wrapper'>
                                                                                                                        <div class='oa-event-date-month-wrapper'>
                                                                                                                            <span class='oa-event-date-month'>Feb    </span>
                                                                                                                        </div>
                                                                                                                        <div class='oa-event-date-day-wrapper'>
                                                                                                                            <span class='oa-event-date-day'>08    </span>
                                                                                                                        </div>
                                                                                                                    </div>
                                                                                                                </div>
                                                                                                            </div>
                                                                                                            <div class="views-field views-field-title">
                                                                                                                <span class="field-content">
                                                                                                                    <a href="https://stevens.campuslabs.com/engage/event/3140142">The Comedy of Errors</a>
                                                                                                                </span>
                                                                                                            </div>
                                                                                                            <div class="views-field views-field-field-oa-date-1">
                                                                                                                <div class="field-content">
                                                                                                                    <span class="date-display-single">
                                                                                                                        <div class="date-display-range">
                                                                                                                            <span class="date-display-start">8:00pm</span>
                                                                                                                            to <span class="date-display-end">9:30pm</span>
                                                                                                                        </div>
                                                                                                                    </span>
                                                                                                                </div>
                                                                                                            </div>
                                                                                                            <div class="views-field views-field-field-feed-name">
                                                                                                                <div class="field-content">Undergraduate DuckLink</div>
                                                                                                            </div>
                                                                                                        </li>
                                                                                                        <li class="views-row views-row-5 views-row-odd">
                                                                                                            <div class="views-field views-field-field-oa-date">
                                                                                                                <div class="field-content">
                                                                                                                    <div class='oa-event-date-wrapper'>
                                                                                                                        <div class='oa-event-date-month-wrapper'>
                                                                                                                            <span class='oa-event-date-month'>Feb    </span>
                                                                                                                        </div>
                                                                                                                        <div class='oa-event-date-day-wrapper'>
                                                                                                                            <span class='oa-event-date-day'>08    </span>
                                                                                                                        </div>
                                                                                                                    </div>
                                                                                                                </div>
                                                                                                            </div>
                                                                                                            <div class="views-field views-field-title">
                                                                                                                <span class="field-content">
                                                                                                                    <a href="https://stevens.campuslabs.com/engage/event/3186661">Anime Club Prolegomenon</a>
                                                                                                                </span>
                                                                                                            </div>
                                                                                                            <div class="views-field views-field-field-oa-date-1">
                                                                                                                <div class="field-content">
                                                                                                                    <span class="date-display-single">
                                                                                                                        <div class="date-display-range">
                                                                                                                            <span class="date-display-start">9:00pm</span>
                                                                                                                            to <span class="date-display-end">11:45pm</span>
                                                                                                                        </div>
                                                                                                                    </span>
                                                                                                                </div>
                                                                                                            </div>
                                                                                                            <div class="views-field views-field-field-feed-name">
                                                                                                                <div class="field-content">Undergraduate DuckLink</div>
                                                                                                            </div>
                                                                                                        </li>
                                                                                                        <li class="views-row views-row-6 views-row-even">
                                                                                                            <div class="views-field views-field-field-oa-date">
                                                                                                                <div class="field-content">
                                                                                                                    <div class='oa-event-date-wrapper'>
                                                                                                                        <div class='oa-event-date-month-wrapper'>
                                                                                                                            <span class='oa-event-date-month'>Feb    </span>
                                                                                                                        </div>
                                                                                                                        <div class='oa-event-date-day-wrapper'>
                                                                                                                            <span class='oa-event-date-day'>08    </span>
                                                                                                                        </div>
                                                                                                                    </div>
                                                                                                                </div>
                                                                                                            </div>
                                                                                                            <div class="views-field views-field-title">
                                                                                                                <span class="field-content">
                                                                                                                    <a href="https://stevens.campuslabs.com/engage/event/3189645">EC DaD: Bumper Cars </a>
                                                                                                                </span>
                                                                                                            </div>
                                                                                                            <div class="views-field views-field-field-oa-date-1">
                                                                                                                <div class="field-content">
                                                                                                                    <span class="date-display-single">
                                                                                                                        <div class="date-display-range">
                                                                                                                            <span class="date-display-start">9:00pm</span>
                                                                                                                            to <span class="date-display-end">11:00pm</span>
                                                                                                                        </div>
                                                                                                                    </span>
                                                                                                                </div>
                                                                                                            </div>
                                                                                                            <div class="views-field views-field-field-feed-name">
                                                                                                                <div class="field-content">Undergraduate DuckLink</div>
                                                                                                            </div>
                                                                                                        </li>
                                                                                                        <li class="views-row views-row-7 views-row-odd">
                                                                                                            <div class="views-field views-field-field-oa-date">
                                                                                                                <div class="field-content">
                                                                                                                    <div class='oa-event-date-wrapper'>
                                                                                                                        <div class='oa-event-date-month-wrapper'>
                                                                                                                            <span class='oa-event-date-month'>Feb    </span>
                                                                                                                        </div>
                                                                                                                        <div class='oa-event-date-day-wrapper'>
                                                                                                                            <span class='oa-event-date-day'>09    </span>
                                                                                                                        </div>
                                                                                                                    </div>
                                                                                                                </div>
                                                                                                            </div>
                                                                                                            <div class="views-field views-field-title">
                                                                                                                <span class="field-content">
                                                                                                                    <a href="https://stevens.campuslabs.com/engage/event/3179004">2019 SASE Northeast Regional Conference: Imagine. Ignite. Illuminate.</a>
                                                                                                                </span>
                                                                                                            </div>
                                                                                                            <div class="views-field views-field-field-oa-date-1">
                                                                                                                <div class="field-content">
                                                                                                                    <span class="date-display-single">
                                                                                                                        <div class="date-display-range">
                                                                                                                            <span class="date-display-start">8:00am</span>
                                                                                                                            to <span class="date-display-end">4:00pm</span>
                                                                                                                        </div>
                                                                                                                    </span>
                                                                                                                </div>
                                                                                                            </div>
                                                                                                            <div class="views-field views-field-field-feed-name">
                                                                                                                <div class="field-content">Undergraduate DuckLink</div>
                                                                                                            </div>
                                                                                                        </li>
                                                                                                        <li class="views-row views-row-8 views-row-even">
                                                                                                            <div class="views-field views-field-field-oa-date">
                                                                                                                <div class="field-content">
                                                                                                                    <div class='oa-event-date-wrapper'>
                                                                                                                        <div class='oa-event-date-month-wrapper'>
                                                                                                                            <span class='oa-event-date-month'>Feb    </span>
                                                                                                                        </div>
                                                                                                                        <div class='oa-event-date-day-wrapper'>
                                                                                                                            <span class='oa-event-date-day'>09    </span>
                                                                                                                        </div>
                                                                                                                    </div>
                                                                                                                </div>
                                                                                                            </div>
                                                                                                            <div class="views-field views-field-title">
                                                                                                                <span class="field-content">
                                                                                                                    <a href="https://stevens.campuslabs.com/engage/event/3182348">Amnesty International Bake Sale</a>
                                                                                                                </span>
                                                                                                            </div>
                                                                                                            <div class="views-field views-field-field-oa-date-1">
                                                                                                                <div class="field-content">
                                                                                                                    <span class="date-display-single">
                                                                                                                        <div class="date-display-range">
                                                                                                                            <span class="date-display-start">10:30am</span>
                                                                                                                            to <span class="date-display-end">6:30pm</span>
                                                                                                                        </div>
                                                                                                                    </span>
                                                                                                                </div>
                                                                                                            </div>
                                                                                                            <div class="views-field views-field-field-feed-name">
                                                                                                                <div class="field-content">Undergraduate DuckLink</div>
                                                                                                            </div>
                                                                                                        </li>
                                                                                                        <li class="views-row views-row-9 views-row-odd">
                                                                                                            <div class="views-field views-field-field-oa-date">
                                                                                                                <div class="field-content">
                                                                                                                    <div class='oa-event-date-wrapper'>
                                                                                                                        <div class='oa-event-date-month-wrapper'>
                                                                                                                            <span class='oa-event-date-month'>Feb    </span>
                                                                                                                        </div>
                                                                                                                        <div class='oa-event-date-day-wrapper'>
                                                                                                                            <span class='oa-event-date-day'>09    </span>
                                                                                                                        </div>
                                                                                                                    </div>
                                                                                                                </div>
                                                                                                            </div>
                                                                                                            <div class="views-field views-field-title">
                                                                                                                <span class="field-content">
                                                                                                                    <a href="https://stevens.campuslabs.com/engage/event/3107210">EC Travel: Ice Skating in Bryant Park</a>
                                                                                                                </span>
                                                                                                            </div>
                                                                                                            <div class="views-field views-field-field-oa-date-1">
                                                                                                                <div class="field-content">
                                                                                                                    <span class="date-display-single">
                                                                                                                        <div class="date-display-range">
                                                                                                                            <span class="date-display-start">12:00pm</span>
                                                                                                                            to <span class="date-display-end">3:00pm</span>
                                                                                                                        </div>
                                                                                                                    </span>
                                                                                                                </div>
                                                                                                            </div>
                                                                                                            <div class="views-field views-field-field-feed-name">
                                                                                                                <div class="field-content">Undergraduate DuckLink</div>
                                                                                                            </div>
                                                                                                        </li>
                                                                                                        <li class="views-row views-row-10 views-row-even views-row-last">
                                                                                                            <div class="views-field views-field-field-oa-date">
                                                                                                                <div class="field-content">
                                                                                                                    <div class='oa-event-date-wrapper'>
                                                                                                                        <div class='oa-event-date-month-wrapper'>
                                                                                                                            <span class='oa-event-date-month'>Feb    </span>
                                                                                                                        </div>
                                                                                                                        <div class='oa-event-date-day-wrapper'>
                                                                                                                            <span class='oa-event-date-day'>09    </span>
                                                                                                                        </div>
                                                                                                                    </div>
                                                                                                                </div>
                                                                                                            </div>
                                                                                                            <div class="views-field views-field-title">
                                                                                                                <span class="field-content">
                                                                                                                    <a href="https://stevens.campuslabs.com/engage/event/3183560">SPC Season 8 Event Tournament 1</a>
                                                                                                                </span>
                                                                                                            </div>
                                                                                                            <div class="views-field views-field-field-oa-date-1">
                                                                                                                <div class="field-content">
                                                                                                                    <span class="date-display-single">
                                                                                                                        <div class="date-display-range">
                                                                                                                            <span class="date-display-start">1:30pm</span>
                                                                                                                            to <span class="date-display-end">8:00pm</span>
                                                                                                                        </div>
                                                                                                                    </span>
                                                                                                                </div>
                                                                                                            </div>
                                                                                                            <div class="views-field views-field-field-feed-name">
                                                                                                                <div class="field-content">Undergraduate DuckLink</div>
                                                                                                            </div>
                                                                                                        </li>
                                                                                                    </ul>
                                                                                                </div>
                                                                                            </div>
                                                                                            <div class="item-list">
                                                                                                <ul class="pagination">
                                                                                                    <li class="pager-previous first">&nbsp;</li>
                                                                                                    <li class="pager-current">
                                                                                                        <span>1 of 31</span>
                                                                                                    </li>
                                                                                                    <li class="pager-next last">
                                                                                                        <a title="Go to next page" href="/portal?og_group_ref_target_id=All&amp;og_group_ref_target_id_mine=0&amp;oa_section_ref_target_id=All&amp;flagged=0&amp;og_subspaces_view_all=0&amp;og_subspaces_view_parent=0&amp;page=1">next ›</a>
                                                                                                    </li>
                                                                                                </ul>
                                                                                                <div class="all-events-btn">
                                                                                                    <span>
                                                                                                        <a href="/events">All Events</a>
                                                                                                    </span>
                                                                                                </div>
                                                                                            </div>
                                                                                        </div>
                                                                                    </div>
                                                                                </section>
                                                                            </div>
                                                                        </div>
                                                                        <div class="col-md-6 radix-layouts-contentcolumn2 panel-panel">
                                                                            <div class="panel-panel-inner">
                                                                                <section class="mystevens-pane  ">
                                                                                    <div class="mystevens-pane-title large-header">
                                                                                        <h2>Tweets      </h2>
                                                                                    </div>
                                                                                    <div class="arrow-down large-arrow"></div>
                                                                                    <div class="mystevens-pane-content clearfix large-pane gray-bg">
                                                                                        <a class="twitter-timeline" data-chrome="noheader" data-theme="light" data-link-color="#a32638" data-tweet-limit="4" href="https://twitter.com/StevensStudents">Twitter</a>
                                                                                        <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
                                                                                    </div>
                                                                                </section>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                    <div class="row">
                                                                        <div class="col-md-12 radix-layouts-contentfooter panel-panel">
                                                                            <div class="panel-panel-inner"></div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                                <!-- /.selby -->
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-12 oa-layout-contentfooter panel-panel">
                                <div class="panel-panel-inner"></div>
                            </div>
                        </div>
                    </main>
                    <div class="col-md-3 oa-layout-sidebar2 panel-panel pull-right">
                        <div class="panel-panel-inner">
                            <div class="oa-responsive-region oa-responsive-desktop oa-responsive-region-right " data-position="right">
                                <div class="oa-responsive-region-inner"></div>
                            </div>
                        </div>
                    </div>
                </div>
                <div id='footer' class="row">
                    <footer class="col-md-12 oa-layout-footer panel-panel">
                        <div class="panel-panel-inner">
                            <div class="oa-horizontal-slice style-region oa-fullwidth">
                                <div class="panel-pane pane-panels-mini pane-oa-footer-panel oa-navbar">
                                    <div class="pane-content">
                                        <div class="panel-display sutro-double clearfix radix-sutro-double" id="mini-panel-oa_footer_panel">
                                            <div class="container-fluid">
                                                <div class="row">
                                                    <div class="col-md-12 radix-layouts-header panel-panel">
                                                        <div class="panel-panel-inner"></div>
                                                    </div>
                                                </div>
                                                <div class="row">
                                                    <div class="col-md-6 radix-layouts-column1 radix-layouts-content panel-panel">
                                                        <div class="panel-panel-inner"></div>
                                                    </div>
                                                    <div class="col-md-6 radix-layouts-column2 radix-layouts-content panel-panel">
                                                        <div class="panel-panel-inner"></div>
                                                    </div>
                                                </div>
                                                <div class="row">
                                                    <div class="col-md-12 radix-layouts-middle panel-panel">
                                                        <div class="panel-panel-inner"></div>
                                                    </div>
                                                </div>
                                                <div class="row">
                                                    <div class="col-md-6 radix-layouts-secondcolumn1 radix-layouts-content panel-panel">
                                                        <div class="panel-panel-inner"></div>
                                                    </div>
                                                    <div class="col-md-6 radix-layouts-secondcolumn2 radix-layouts-content panel-panel">
                                                        <div class="panel-panel-inner"></div>
                                                    </div>
                                                </div>
                                                <div class="row">
                                                    <div class="col-md-12 radix-layouts-footer panel-panel">
                                                        <div class="panel-panel-inner">
                                                            <div class="panel-pane pane-block pane-system-main-menu pull-right">
                                                                <div class="pane-content">
                                                                    <ul class="menu">
                                                                        <li class="first leaf dhtml-menu" id="dhtml_menu-9581">
                                                                            <a href="http://www.stevens.edu" title="">Stevens.edu</a>
                                                                        </li>
                                                                        <li class="leaf dhtml-menu" id="dhtml_menu-31511">
                                                                            <a href="https://web.stevens.edu/peoplefinder/" title="">People Finder</a>
                                                                        </li>
                                                                        <li class="leaf dhtml-menu" id="dhtml_menu-31516">
                                                                            <a href="/search/site?source=menu" title="">Search</a>
                                                                        </li>
                                                                        <li class="last leaf dhtml-menu" id="dhtml_menu-31716">
                                                                            <a href="/directory" title="">Campus Directory</a>
                                                                        </li>
                                                                    </ul>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <!-- /.sutro-double -->
                                    </div>
                                </div>
                            </div>
                        </div>
                    </footer>
                </div>
                <div class="row">
                    <div class="col-md-12 oa-layout-traybottom panel-panel">
                        <div class="panel-panel-inner">
                            <div class="oa-responsive-region oa-responsive-desktop oa-responsive-region-bottom oa-responsive-fixed oa-responsive-expand " data-position="bottom">
                                <div class="oa-responsive-region-inner"></div>
                            </div>
                            <div class="oa-hidden " data-position="bottom">
                                <div class="oa-responsive-region-inner"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <script type="text/javascript" src="https://my.stevens.edu/profiles/openatrium/modules/panopoly/panopoly_widgets/panopoly-widgets.js?pm2omv"></script>
        <script type="text/javascript" src="https://my.stevens.edu/profiles/openatrium/modules/panopoly/panopoly_widgets/panopoly-widgets-spotlight.js?pm2omv"></script>
        <script type="text/javascript">
            window.NREUM || (NREUM = {});
            NREUM.info = {
                "beacon": "bam.nr-data.net",
                "licenseKey": "a434b8a417",
                "applicationID": "5225182",
                "transactionName": "ZFRTZ0EEVhJXWkJcDF0ecFBHDFcPGUlXUgZsXFBdUgJdE2lXWVEGbEdYVkQ6SABRXA==",
                "queueTime": 0,
                "applicationTime": 1431,
                "atts": "SBNQEQkeRRw=",
                "errorBeacon": "bam.nr-data.net",
                "agent": ""
            }
        </script>
    </body>
</html>
```

## Ajax Script

The following script is located under `top/my.stevens.edu/misc/`, and are titles `ajax.js`, `drupal.js`, and `progress.js` respectively.

### ajax.js

```js
(function($) {

    /**
 * Provides Ajax page updating via jQuery $.ajax (Asynchronous JavaScript and XML).
 *
 * Ajax is a method of making a request via JavaScript while viewing an HTML
 * page. The request returns an array of commands encoded in JSON, which is
 * then executed to make any changes that are necessary to the page.
 *
 * Drupal uses this file to enhance form elements with #ajax['path'] and
 * #ajax['wrapper'] properties. If set, this file will automatically be included
 * to provide Ajax capabilities.
 */

    Drupal.ajax = Drupal.ajax || {};

    Drupal.settings.urlIsAjaxTrusted = Drupal.settings.urlIsAjaxTrusted || {};

    /**
 * Attaches the Ajax behavior to each Ajax form element.
 */
    Drupal.behaviors.AJAX = {
        attach: function(context, settings) {
            // Load all Ajax behaviors specified in the settings.
            for (var base in settings.ajax) {
                if (!$('#' + base + '.ajax-processed').length) {
                    var element_settings = settings.ajax[base];

                    if (typeof element_settings.selector == 'undefined') {
                        element_settings.selector = '#' + base;
                    }
                    $(element_settings.selector).each(function() {
                        element_settings.element = this;
                        Drupal.ajax[base] = new Drupal.ajax(base,this,element_settings);
                    });

                    $('#' + base).addClass('ajax-processed');
                }
            }

            // Bind Ajax behaviors to all items showing the class.
            $('.use-ajax:not(.ajax-processed)').addClass('ajax-processed').each(function() {
                var element_settings = {};
                // Clicked links look better with the throbber than the progress bar.
                element_settings.progress = {
                    'type': 'throbber'
                };

                // For anchor tags, these will go to the target of the anchor rather
                // than the usual location.
                if ($(this).attr('href')) {
                    element_settings.url = $(this).attr('href');
                    element_settings.event = 'click';
                }
                var base = $(this).attr('id');
                Drupal.ajax[base] = new Drupal.ajax(base,this,element_settings);
            });

            // This class means to submit the form to the action using Ajax.
            $('.use-ajax-submit:not(.ajax-processed)').addClass('ajax-processed').each(function() {
                var element_settings = {};

                // Ajax submits specified in this manner automatically submit to the
                // normal form action.
                element_settings.url = $(this.form).attr('action');
                // Form submit button clicks need to tell the form what was clicked so
                // it gets passed in the POST request.
                element_settings.setClick = true;
                // Form buttons use the 'click' event rather than mousedown.
                element_settings.event = 'click';
                // Clicked form buttons look better with the throbber than the progress bar.
                element_settings.progress = {
                    'type': 'throbber'
                };

                var base = $(this).attr('id');
                Drupal.ajax[base] = new Drupal.ajax(base,this,element_settings);
            });
        }
    };

    /**
 * Ajax object.
 *
 * All Ajax objects on a page are accessible through the global Drupal.ajax
 * object and are keyed by the submit button's ID. You can access them from
 * your module's JavaScript file to override properties or functions.
 *
 * For example, if your Ajax enabled button has the ID 'edit-submit', you can
 * redefine the function that is called to insert the new content like this
 * (inside a Drupal.behaviors attach block):
 * @code
 *    Drupal.behaviors.myCustomAJAXStuff = {
 *      attach: function (context, settings) {
 *        Drupal.ajax['edit-submit'].commands.insert = function (ajax, response, status) {
 *          new_content = $(response.data);
 *          $('#my-wrapper').append(new_content);
 *          alert('New content was appended to #my-wrapper');
 *        }
 *      }
 *    };
 * @endcode
 */
    Drupal.ajax = function(base, element, element_settings) {
        var defaults = {
            url: 'system/ajax',
            event: 'mousedown',
            keypress: true,
            selector: '#' + base,
            effect: 'none',
            speed: 'none',
            method: 'replaceWith',
            progress: {
                type: 'throbber',
                message: Drupal.t('Please wait...')
            },
            submit: {
                'js': true
            }
        };

        $.extend(this, defaults, element_settings);

        this.element = element;
        this.element_settings = element_settings;

        // Replacing 'nojs' with 'ajax' in the URL allows for an easy method to let
        // the server detect when it needs to degrade gracefully.
        // There are five scenarios to check for:
        // 1. /nojs/
        // 2. /nojs$ - The end of a URL string.
        // 3. /nojs? - Followed by a query (with clean URLs enabled).
        //      E.g.: path/nojs?destination=foobar
        // 4. /nojs& - Followed by a query (without clean URLs enabled).
        //      E.g.: ?q=path/nojs&destination=foobar
        // 5. /nojs# - Followed by a fragment.
        //      E.g.: path/nojs#myfragment
        this.url = element_settings.url.replace(/\/nojs(\/|$|\?|&|#)/g, '/ajax$1');
        // If the 'nojs' version of the URL is trusted, also trust the 'ajax' version.
        if (Drupal.settings.urlIsAjaxTrusted[element_settings.url]) {
            Drupal.settings.urlIsAjaxTrusted[this.url] = true;
        }

        this.wrapper = '#' + element_settings.wrapper;

        // If there isn't a form, jQuery.ajax() will be used instead, allowing us to
        // bind Ajax to links as well.
        if (this.element.form) {
            this.form = $(this.element.form);
        }

        // Set the options for the ajaxSubmit function.
        // The 'this' variable will not persist inside of the options object.
        var ajax = this;
        ajax.options = {
            url: ajax.url,
            data: ajax.submit,
            beforeSerialize: function(element_settings, options) {
                return ajax.beforeSerialize(element_settings, options);
            },
            beforeSubmit: function(form_values, element_settings, options) {
                ajax.ajaxing = true;
                return ajax.beforeSubmit(form_values, element_settings, options);
            },
            beforeSend: function(xmlhttprequest, options) {
                ajax.ajaxing = true;
                return ajax.beforeSend(xmlhttprequest, options);
            },
            success: function(response, status, xmlhttprequest) {
                // Sanity check for browser support (object expected).
                // When using iFrame uploads, responses must be returned as a string.
                if (typeof response == 'string') {
                    response = $.parseJSON(response);
                }

                // Prior to invoking the response's commands, verify that they can be
                // trusted by checking for a response header. See
                // ajax_set_verification_header() for details.
                // - Empty responses are harmless so can bypass verification. This avoids
                //   an alert message for server-generated no-op responses that skip Ajax
                //   rendering.
                // - Ajax objects with trusted URLs (e.g., ones defined server-side via
                //   #ajax) can bypass header verification. This is especially useful for
                //   Ajax with multipart forms. Because IFRAME transport is used, the
                //   response headers cannot be accessed for verification.
                if (response !== null && !Drupal.settings.urlIsAjaxTrusted[ajax.url]) {
                    if (xmlhttprequest.getResponseHeader('X-Drupal-Ajax-Token') !== '1') {
                        var customMessage = Drupal.t("The response failed verification so will not be processed.");
                        return ajax.error(xmlhttprequest, ajax.url, customMessage);
                    }
                }

                return ajax.success(response, status);
            },
            complete: function(xmlhttprequest, status) {
                ajax.ajaxing = false;
                if (status == 'error' || status == 'parsererror') {
                    return ajax.error(xmlhttprequest, ajax.url);
                }
            },
            dataType: 'json',
            type: 'POST'
        };

        // Bind the ajaxSubmit function to the element event.
        $(ajax.element).bind(element_settings.event, function(event) {
            if (!Drupal.settings.urlIsAjaxTrusted[ajax.url] && !Drupal.urlIsLocal(ajax.url)) {
                throw new Error(Drupal.t('The callback URL is not local and not trusted: !url', {
                    '!url': ajax.url
                }));
            }
            return ajax.eventResponse(this, event);
        });

        // If necessary, enable keyboard submission so that Ajax behaviors
        // can be triggered through keyboard input as well as e.g. a mousedown
        // action.
        if (element_settings.keypress) {
            $(ajax.element).keypress(function(event) {
                return ajax.keypressResponse(this, event);
            });
        }

        // If necessary, prevent the browser default action of an additional event.
        // For example, prevent the browser default action of a click, even if the
        // AJAX behavior binds to mousedown.
        if (element_settings.prevent) {
            $(ajax.element).bind(element_settings.prevent, false);
        }
    }
    ;

    /**
 * Handle a key press.
 *
 * The Ajax object will, if instructed, bind to a key press response. This
 * will test to see if the key press is valid to trigger this event and
 * if it is, trigger it for us and prevent other keypresses from triggering.
 * In this case we're handling RETURN and SPACEBAR keypresses (event codes 13
 * and 32. RETURN is often used to submit a form when in a textfield, and 
 * SPACE is often used to activate an element without submitting. 
 */
    Drupal.ajax.prototype.keypressResponse = function(element, event) {
        // Create a synonym for this to reduce code confusion.
        var ajax = this;

        // Detect enter key and space bar and allow the standard response for them,
        // except for form elements of type 'text' and 'textarea', where the 
        // spacebar activation causes inappropriate activation if #ajax['keypress'] is 
        // TRUE. On a text-type widget a space should always be a space.
        if (event.which == 13 || (event.which == 32 && element.type != 'text' && element.type != 'textarea')) {
            $(ajax.element_settings.element).trigger(ajax.element_settings.event);
            return false;
        }
    }
    ;

    /**
 * Handle an event that triggers an Ajax response.
 *
 * When an event that triggers an Ajax response happens, this method will
 * perform the actual Ajax call. It is bound to the event using
 * bind() in the constructor, and it uses the options specified on the
 * ajax object.
 */
    Drupal.ajax.prototype.eventResponse = function(element, event) {
        // Create a synonym for this to reduce code confusion.
        var ajax = this;

        // Do not perform another ajax command if one is already in progress.
        if (ajax.ajaxing) {
            return false;
        }

        try {
            if (ajax.form) {
                // If setClick is set, we must set this to ensure that the button's
                // value is passed.
                if (ajax.setClick) {
                    // Mark the clicked button. 'form.clk' is a special variable for
                    // ajaxSubmit that tells the system which element got clicked to
                    // trigger the submit. Without it there would be no 'op' or
                    // equivalent.
                    element.form.clk = element;
                }

                ajax.form.ajaxSubmit(ajax.options);
            } else {
                ajax.beforeSerialize(ajax.element, ajax.options);
                $.ajax(ajax.options);
            }
        } catch (e) {
            // Unset the ajax.ajaxing flag here because it won't be unset during
            // the complete response.
            ajax.ajaxing = false;
            alert("An error occurred while attempting to process " + ajax.options.url + ": " + e.message);
        }

        // For radio/checkbox, allow the default event. On IE, this means letting
        // it actually check the box.
        if (typeof element.type != 'undefined' && (element.type == 'checkbox' || element.type == 'radio')) {
            return true;
        } else {
            return false;
        }

    }
    ;

    /**
 * Handler for the form serialization.
 *
 * Runs before the beforeSend() handler (see below), and unlike that one, runs
 * before field data is collected.
 */
    Drupal.ajax.prototype.beforeSerialize = function(element, options) {
        // Allow detaching behaviors to update field values before collecting them.
        // This is only needed when field values are added to the POST data, so only
        // when there is a form such that this.form.ajaxSubmit() is used instead of
        // $.ajax(). When there is no form and $.ajax() is used, beforeSerialize()
        // isn't called, but don't rely on that: explicitly check this.form.
        if (this.form) {
            var settings = this.settings || Drupal.settings;
            Drupal.detachBehaviors(this.form, settings, 'serialize');
        }

        // Prevent duplicate HTML ids in the returned markup.
        // @see drupal_html_id()
        options.data['ajax_html_ids[]'] = [];
        $('[id]').each(function() {
            options.data['ajax_html_ids[]'].push(this.id);
        });

        // Allow Drupal to return new JavaScript and CSS files to load without
        // returning the ones already loaded.
        // @see ajax_base_page_theme()
        // @see drupal_get_css()
        // @see drupal_get_js()
        options.data['ajax_page_state[theme]'] = Drupal.settings.ajaxPageState.theme;
        options.data['ajax_page_state[theme_token]'] = Drupal.settings.ajaxPageState.theme_token;
        for (var key in Drupal.settings.ajaxPageState.css) {
            options.data['ajax_page_state[css][' + key + ']'] = 1;
        }
        for (var key in Drupal.settings.ajaxPageState.js) {
            options.data['ajax_page_state[js][' + key + ']'] = 1;
        }
    }
    ;

    /**
 * Modify form values prior to form submission.
 */
    Drupal.ajax.prototype.beforeSubmit = function(form_values, element, options) {// This function is left empty to make it simple to override for modules
    // that wish to add functionality here.
    }
    ;

    /**
 * Prepare the Ajax request before it is sent.
 */
    Drupal.ajax.prototype.beforeSend = function(xmlhttprequest, options) {
        // For forms without file inputs, the jQuery Form plugin serializes the form
        // values, and then calls jQuery's $.ajax() function, which invokes this
        // handler. In this circumstance, options.extraData is never used. For forms
        // with file inputs, the jQuery Form plugin uses the browser's normal form
        // submission mechanism, but captures the response in a hidden IFRAME. In this
        // circumstance, it calls this handler first, and then appends hidden fields
        // to the form to submit the values in options.extraData. There is no simple
        // way to know which submission mechanism will be used, so we add to extraData
        // regardless, and allow it to be ignored in the former case.
        if (this.form) {
            options.extraData = options.extraData || {};

            // Let the server know when the IFRAME submission mechanism is used. The
            // server can use this information to wrap the JSON response in a TEXTAREA,
            // as per http://jquery.malsup.com/form/#file-upload.
            options.extraData.ajax_iframe_upload = '1';

            // The triggering element is about to be disabled (see below), but if it
            // contains a value (e.g., a checkbox, textfield, select, etc.), ensure that
            // value is included in the submission. As per above, submissions that use
            // $.ajax() are already serialized prior to the element being disabled, so
            // this is only needed for IFRAME submissions.
            var v = $.fieldValue(this.element);
            if (v !== null) {
                options.extraData[this.element.name] = Drupal.checkPlain(v);
            }
        }

        // Disable the element that received the change to prevent user interface
        // interaction while the Ajax request is in progress. ajax.ajaxing prevents
        // the element from triggering a new request, but does not prevent the user
        // from changing its value.
        $(this.element).addClass('progress-disabled').attr('disabled', true);

        // Insert progressbar or throbber.
        if (this.progress.type == 'bar') {
            var progressBar = new Drupal.progressBar('ajax-progress-' + this.element.id,eval(this.progress.update_callback),this.progress.method,eval(this.progress.error_callback));
            if (this.progress.message) {
                progressBar.setProgress(-1, this.progress.message);
            }
            if (this.progress.url) {
                progressBar.startMonitoring(this.progress.url, this.progress.interval || 1500);
            }
            this.progress.element = $(progressBar.element).addClass('ajax-progress ajax-progress-bar');
            this.progress.object = progressBar;
            $(this.element).after(this.progress.element);
        } else if (this.progress.type == 'throbber') {
            this.progress.element = $('<div class="ajax-progress ajax-progress-throbber"><div class="throbber">&nbsp;</div></div>');
            if (this.progress.message) {
                $('.throbber', this.progress.element).after('<div class="message">' + this.progress.message + '</div>');
            }
            $(this.element).after(this.progress.element);
        }
    }
    ;

    /**
 * Handler for the form redirection completion.
 */
    Drupal.ajax.prototype.success = function(response, status) {
        // Remove the progress element.
        if (this.progress.element) {
            $(this.progress.element).remove();
        }
        if (this.progress.object) {
            this.progress.object.stopMonitoring();
        }
        $(this.element).removeClass('progress-disabled').removeAttr('disabled');

        Drupal.freezeHeight();

        for (var i in response) {
            if (response.hasOwnProperty(i) && response[i]['command'] && this.commands[response[i]['command']]) {
                this.commands[response[i]['command']](this, response[i], status);
            }
        }

        // Reattach behaviors, if they were detached in beforeSerialize(). The
        // attachBehaviors() called on the new content from processing the response
        // commands is not sufficient, because behaviors from the entire form need
        // to be reattached.
        if (this.form) {
            var settings = this.settings || Drupal.settings;
            Drupal.attachBehaviors(this.form, settings);
        }

        Drupal.unfreezeHeight();

        // Remove any response-specific settings so they don't get used on the next
        // call by mistake.
        this.settings = null;
    }
    ;

    /**
 * Build an effect object which tells us how to apply the effect when adding new HTML.
 */
    Drupal.ajax.prototype.getEffect = function(response) {
        var type = response.effect || this.effect;
        var speed = response.speed || this.speed;

        var effect = {};
        if (type == 'none') {
            effect.showEffect = 'show';
            effect.hideEffect = 'hide';
            effect.showSpeed = '';
        } else if (type == 'fade') {
            effect.showEffect = 'fadeIn';
            effect.hideEffect = 'fadeOut';
            effect.showSpeed = speed;
        } else {
            effect.showEffect = type + 'Toggle';
            effect.hideEffect = type + 'Toggle';
            effect.showSpeed = speed;
        }

        return effect;
    }
    ;

    /**
 * Handler for the form redirection error.
 */
    Drupal.ajax.prototype.error = function(xmlhttprequest, uri, customMessage) {
        Drupal.displayAjaxError(Drupal.ajaxError(xmlhttprequest, uri, customMessage));
        // Remove the progress element.
        if (this.progress.element) {
            $(this.progress.element).remove();
        }
        if (this.progress.object) {
            this.progress.object.stopMonitoring();
        }
        // Undo hide.
        $(this.wrapper).show();
        // Re-enable the element.
        $(this.element).removeClass('progress-disabled').removeAttr('disabled');
        // Reattach behaviors, if they were detached in beforeSerialize().
        if (this.form) {
            var settings = this.settings || Drupal.settings;
            Drupal.attachBehaviors(this.form, settings);
        }
    }
    ;

    /**
 * Provide a series of commands that the server can request the client perform.
 */
    Drupal.ajax.prototype.commands = {
        /**
   * Command to insert new content into the DOM.
   */
        insert: function(ajax, response, status) {
            // Get information from the response. If it is not there, default to
            // our presets.
            var wrapper = response.selector ? $(response.selector) : $(ajax.wrapper);
            var method = response.method || ajax.method;
            var effect = ajax.getEffect(response);

            // We don't know what response.data contains: it might be a string of text
            // without HTML, so don't rely on jQuery correctly iterpreting
            // $(response.data) as new HTML rather than a CSS selector. Also, if
            // response.data contains top-level text nodes, they get lost with either
            // $(response.data) or $('<div></div>').replaceWith(response.data).
            var new_content_wrapped = $('<div></div>').html(response.data);
            var new_content = new_content_wrapped.contents();

            // For legacy reasons, the effects processing code assumes that new_content
            // consists of a single top-level element. Also, it has not been
            // sufficiently tested whether attachBehaviors() can be successfully called
            // with a context object that includes top-level text nodes. However, to
            // give developers full control of the HTML appearing in the page, and to
            // enable Ajax content to be inserted in places where DIV elements are not
            // allowed (e.g., within TABLE, TR, and SPAN parents), we check if the new
            // content satisfies the requirement of a single top-level element, and
            // only use the container DIV created above when it doesn't. For more
            // information, please see http://drupal.org/node/736066.
            if (new_content.length != 1 || new_content.get(0).nodeType != 1) {
                new_content = new_content_wrapped;
            }

            // If removing content from the wrapper, detach behaviors first.
            switch (method) {
            case 'html':
            case 'replaceWith':
            case 'replaceAll':
            case 'empty':
            case 'remove':
                var settings = response.settings || ajax.settings || Drupal.settings;
                Drupal.detachBehaviors(wrapper, settings);
            }

            // Add the new content to the page.
            wrapper[method](new_content);

            // Immediately hide the new content if we're using any effects.
            if (effect.showEffect != 'show') {
                new_content.hide();
            }

            // Determine which effect to use and what content will receive the
            // effect, then show the new content.
            if ($('.ajax-new-content', new_content).length > 0) {
                $('.ajax-new-content', new_content).hide();
                new_content.show();
                $('.ajax-new-content', new_content)[effect.showEffect](effect.showSpeed);
            } else if (effect.showEffect != 'show') {
                new_content[effect.showEffect](effect.showSpeed);
            }

            // Attach all JavaScript behaviors to the new content, if it was successfully
            // added to the page, this if statement allows #ajax['wrapper'] to be
            // optional.
            if (new_content.parents('html').length > 0) {
                // Apply any settings from the returned JSON if available.
                var settings = response.settings || ajax.settings || Drupal.settings;
                Drupal.attachBehaviors(new_content, settings);
            }
        },

        /**
   * Command to remove a chunk from the page.
   */
        remove: function(ajax, response, status) {
            var settings = response.settings || ajax.settings || Drupal.settings;
            Drupal.detachBehaviors($(response.selector), settings);
            $(response.selector).remove();
        },

        /**
   * Command to mark a chunk changed.
   */
        changed: function(ajax, response, status) {
            if (!$(response.selector).hasClass('ajax-changed')) {
                $(response.selector).addClass('ajax-changed');
                if (response.asterisk) {
                    $(response.selector).find(response.asterisk).append(' <span class="ajax-changed">*</span> ');
                }
            }
        },

        /**
   * Command to provide an alert.
   */
        alert: function(ajax, response, status) {
            alert(response.text, response.title);
        },

        /**
   * Command to provide the jQuery css() function.
   */
        css: function(ajax, response, status) {
            $(response.selector).css(response.argument);
        },

        /**
   * Command to set the settings that will be used for other commands in this response.
   */
        settings: function(ajax, response, status) {
            if (response.merge) {
                $.extend(true, Drupal.settings, response.settings);
            } else {
                ajax.settings = response.settings;
            }
        },

        /**
   * Command to attach data using jQuery's data API.
   */
        data: function(ajax, response, status) {
            $(response.selector).data(response.name, response.value);
        },

        /**
   * Command to apply a jQuery method.
   */
        invoke: function(ajax, response, status) {
            var $element = $(response.selector);
            $element[response.method].apply($element, response.arguments);
        },

        /**
   * Command to restripe a table.
   */
        restripe: function(ajax, response, status) {
            // :even and :odd are reversed because jQuery counts from 0 and
            // we count from 1, so we're out of sync.
            // Match immediate children of the parent element to allow nesting.
            $('> tbody > tr:visible, > tr:visible', $(response.selector)).removeClass('odd even').filter(':even').addClass('odd').end().filter(':odd').addClass('even');
        },

        /**
   * Command to add css.
   *
   * Uses the proprietary addImport method if available as browsers which
   * support that method ignore @import statements in dynamically added
   * stylesheets.
   */
        add_css: function(ajax, response, status) {
            // Add the styles in the normal way.
            $('head').prepend(response.data);
            // Add imports in the styles using the addImport method if available.
            var match, importMatch = /^@import url\("(.*)"\);$/igm;
            if (document.styleSheets[0].addImport && importMatch.test(response.data)) {
                importMatch.lastIndex = 0;
                while (match = importMatch.exec(response.data)) {
                    document.styleSheets[0].addImport(match[1]);
                }
            }
        },

        /**
   * Command to update a form's build ID.
   */
        updateBuildId: function(ajax, response, status) {
            $('input[name="form_build_id"][value="' + response['old'] + '"]').val(response['new']);
        }
    };

}
)(jQuery);
```

### drupal.js
```js
var Drupal = Drupal || {
    'settings': {},
    'behaviors': {},
    'locale': {}
};

// Allow other JavaScript libraries to use $.
jQuery.noConflict();

(function($) {

    /**
 * Override jQuery.fn.init to guard against XSS attacks.
 *
 * See http://bugs.jquery.com/ticket/9521
 */
    var jquery_init = $.fn.init;
    $.fn.init = function(selector, context, rootjQuery) {
        // If the string contains a "#" before a "<", treat it as invalid HTML.
        if (selector && typeof selector === 'string') {
            var hash_position = selector.indexOf('#');
            if (hash_position >= 0) {
                var bracket_position = selector.indexOf('<');
                if (bracket_position > hash_position) {
                    throw 'Syntax error, unrecognized expression: ' + selector;
                }
            }
        }
        return jquery_init.call(this, selector, context, rootjQuery);
    }
    ;
    $.fn.init.prototype = jquery_init.prototype;

    /**
 * Pre-filter Ajax requests to guard against XSS attacks.
 *
 * See https://github.com/jquery/jquery/issues/2432
 */
    if ($.ajaxPrefilter) {
        // For newer versions of jQuery, use an Ajax prefilter to prevent
        // auto-executing script tags from untrusted domains. This is similar to the
        // fix that is built in to jQuery 3.0 and higher.
        $.ajaxPrefilter(function(s) {
            if (s.crossDomain) {
                s.contents.script = false;
            }
        });
    } else if ($.httpData) {
        // For the version of jQuery that ships with Drupal core, override
        // jQuery.httpData to prevent auto-detecting "script" data types from
        // untrusted domains.
        var jquery_httpData = $.httpData;
        $.httpData = function(xhr, type, s) {
            // @todo Consider backporting code from newer jQuery versions to check for
            //   a cross-domain request here, rather than using Drupal.urlIsLocal() to
            //   block scripts from all URLs that are not on the same site.
            if (!type && !Drupal.urlIsLocal(s.url)) {
                var content_type = xhr.getResponseHeader('content-type') || '';
                if (content_type.indexOf('javascript') >= 0) {
                    // Default to a safe data type.
                    type = 'text';
                }
            }
            return jquery_httpData.call(this, xhr, type, s);
        }
        ;
        $.httpData.prototype = jquery_httpData.prototype;
    }

    /**
 * Attach all registered behaviors to a page element.
 *
 * Behaviors are event-triggered actions that attach to page elements, enhancing
 * default non-JavaScript UIs. Behaviors are registered in the Drupal.behaviors
 * object using the method 'attach' and optionally also 'detach' as follows:
 * @code
 *    Drupal.behaviors.behaviorName = {
 *      attach: function (context, settings) {
 *        ...
 *      },
 *      detach: function (context, settings, trigger) {
 *        ...
 *      }
 *    };
 * @endcode
 *
 * Drupal.attachBehaviors is added below to the jQuery ready event and so
 * runs on initial page load. Developers implementing AHAH/Ajax in their
 * solutions should also call this function after new page content has been
 * loaded, feeding in an element to be processed, in order to attach all
 * behaviors to the new content.
 *
 * Behaviors should use
 * @code
 *   $(selector).once('behavior-name', function () {
 *     ...
 *   });
 * @endcode
 * to ensure the behavior is attached only once to a given element. (Doing so
 * enables the reprocessing of given elements, which may be needed on occasion
 * despite the ability to limit behavior attachment to a particular element.)
 *
 * @param context
 *   An element to attach behaviors to. If none is given, the document element
 *   is used.
 * @param settings
 *   An object containing settings for the current context. If none given, the
 *   global Drupal.settings object is used.
 */
    Drupal.attachBehaviors = function(context, settings) {
        context = context || document;
        settings = settings || Drupal.settings;
        // Execute all of them.
        $.each(Drupal.behaviors, function() {
            if ($.isFunction(this.attach)) {
                this.attach(context, settings);
            }
        });
    }
    ;

    /**
 * Detach registered behaviors from a page element.
 *
 * Developers implementing AHAH/Ajax in their solutions should call this
 * function before page content is about to be removed, feeding in an element
 * to be processed, in order to allow special behaviors to detach from the
 * content.
 *
 * Such implementations should look for the class name that was added in their
 * corresponding Drupal.behaviors.behaviorName.attach implementation, i.e.
 * behaviorName-processed, to ensure the behavior is detached only from
 * previously processed elements.
 *
 * @param context
 *   An element to detach behaviors from. If none is given, the document element
 *   is used.
 * @param settings
 *   An object containing settings for the current context. If none given, the
 *   global Drupal.settings object is used.
 * @param trigger
 *   A string containing what's causing the behaviors to be detached. The
 *   possible triggers are:
 *   - unload: (default) The context element is being removed from the DOM.
 *   - move: The element is about to be moved within the DOM (for example,
 *     during a tabledrag row swap). After the move is completed,
 *     Drupal.attachBehaviors() is called, so that the behavior can undo
 *     whatever it did in response to the move. Many behaviors won't need to
 *     do anything simply in response to the element being moved, but because
 *     IFRAME elements reload their "src" when being moved within the DOM,
 *     behaviors bound to IFRAME elements (like WYSIWYG editors) may need to
 *     take some action.
 *   - serialize: When an Ajax form is submitted, this is called with the
 *     form as the context. This provides every behavior within the form an
 *     opportunity to ensure that the field elements have correct content
 *     in them before the form is serialized. The canonical use-case is so
 *     that WYSIWYG editors can update the hidden textarea to which they are
 *     bound.
 *
 * @see Drupal.attachBehaviors
 */
    Drupal.detachBehaviors = function(context, settings, trigger) {
        context = context || document;
        settings = settings || Drupal.settings;
        trigger = trigger || 'unload';
        // Execute all of them.
        $.each(Drupal.behaviors, function() {
            if ($.isFunction(this.detach)) {
                this.detach(context, settings, trigger);
            }
        });
    }
    ;

    /**
 * Encode special characters in a plain-text string for display as HTML.
 *
 * @ingroup sanitization
 */
    Drupal.checkPlain = function(str) {
        var character, regex, replace = {
            '&': '&amp;',
            "'": '&#39;',
            '"': '&quot;',
            '<': '&lt;',
            '>': '&gt;'
        };
        str = String(str);
        for (character in replace) {
            if (replace.hasOwnProperty(character)) {
                regex = new RegExp(character,'g');
                str = str.replace(regex, replace[character]);
            }
        }
        return str;
    }
    ;

    /**
 * Replace placeholders with sanitized values in a string.
 *
 * @param str
 *   A string with placeholders.
 * @param args
 *   An object of replacements pairs to make. Incidences of any key in this
 *   array are replaced with the corresponding value. Based on the first
 *   character of the key, the value is escaped and/or themed:
 *    - !variable: inserted as is
 *    - @variable: escape plain text to HTML (Drupal.checkPlain)
 *    - %variable: escape text and theme as a placeholder for user-submitted
 *      content (checkPlain + Drupal.theme('placeholder'))
 *
 * @see Drupal.t()
 * @ingroup sanitization
 */
    Drupal.formatString = function(str, args) {
        // Transform arguments before inserting them.
        for (var key in args) {
            if (args.hasOwnProperty(key)) {
                switch (key.charAt(0)) {
                    // Escaped only.
                case '@':
                    args[key] = Drupal.checkPlain(args[key]);
                    break;
                    // Pass-through.
                case '!':
                    break;
                    // Escaped and placeholder.
                default:
                    args[key] = Drupal.theme('placeholder', args[key]);
                    break;
                }
            }
        }

        return Drupal.stringReplace(str, args, null);
    }
    ;

    /**
 * Replace substring.
 *
 * The longest keys will be tried first. Once a substring has been replaced,
 * its new value will not be searched again.
 *
 * @param {String} str
 *   A string with placeholders.
 * @param {Object} args
 *   Key-value pairs.
 * @param {Array|null} keys
 *   Array of keys from the "args".  Internal use only.
 *
 * @return {String}
 *   Returns the replaced string.
 */
    Drupal.stringReplace = function(str, args, keys) {
        if (str.length === 0) {
            return str;
        }

        // If the array of keys is not passed then collect the keys from the args.
        if (!$.isArray(keys)) {
            keys = [];
            for (var k in args) {
                if (args.hasOwnProperty(k)) {
                    keys.push(k);
                }
            }

            // Order the keys by the character length. The shortest one is the first.
            keys.sort(function(a, b) {
                return a.length - b.length;
            });
        }

        if (keys.length === 0) {
            return str;
        }

        // Take next longest one from the end.
        var key = keys.pop();
        var fragments = str.split(key);

        if (keys.length) {
            for (var i = 0; i < fragments.length; i++) {
                // Process each fragment with a copy of remaining keys.
                fragments[i] = Drupal.stringReplace(fragments[i], args, keys.slice(0));
            }
        }

        return fragments.join(args[key]);
    }
    ;

    /**
 * Translate strings to the page language or a given language.
 *
 * See the documentation of the server-side t() function for further details.
 *
 * @param str
 *   A string containing the English string to translate.
 * @param args
 *   An object of replacements pairs to make after translation. Incidences
 *   of any key in this array are replaced with the corresponding value.
 *   See Drupal.formatString().
 *
 * @param options
 *   - 'context' (defaults to the empty context): The context the source string
 *     belongs to.
 *
 * @return
 *   The translated string.
 */
    Drupal.t = function(str, args, options) {
        options = options || {};
        options.context = options.context || '';

        // Fetch the localized version of the string.
        if (Drupal.locale.strings && Drupal.locale.strings[options.context] && Drupal.locale.strings[options.context][str]) {
            str = Drupal.locale.strings[options.context][str];
        }

        if (args) {
            str = Drupal.formatString(str, args);
        }
        return str;
    }
    ;

    /**
 * Format a string containing a count of items.
 *
 * This function ensures that the string is pluralized correctly. Since Drupal.t() is
 * called by this function, make sure not to pass already-localized strings to it.
 *
 * See the documentation of the server-side format_plural() function for further details.
 *
 * @param count
 *   The item count to display.
 * @param singular
 *   The string for the singular case. Please make sure it is clear this is
 *   singular, to ease translation (e.g. use "1 new comment" instead of "1 new").
 *   Do not use @count in the singular string.
 * @param plural
 *   The string for the plural case. Please make sure it is clear this is plural,
 *   to ease translation. Use @count in place of the item count, as in "@count
 *   new comments".
 * @param args
 *   An object of replacements pairs to make after translation. Incidences
 *   of any key in this array are replaced with the corresponding value.
 *   See Drupal.formatString().
 *   Note that you do not need to include @count in this array.
 *   This replacement is done automatically for the plural case.
 * @param options
 *   The options to pass to the Drupal.t() function.
 * @return
 *   A translated string.
 */
    Drupal.formatPlural = function(count, singular, plural, args, options) {
        args = args || {};
        args['@count'] = count;
        // Determine the index of the plural form.
        var index = Drupal.locale.pluralFormula ? Drupal.locale.pluralFormula(args['@count']) : ((args['@count'] == 1) ? 0 : 1);

        if (index == 0) {
            return Drupal.t(singular, args, options);
        } else if (index == 1) {
            return Drupal.t(plural, args, options);
        } else {
            args['@count[' + index + ']'] = args['@count'];
            delete args['@count'];
            return Drupal.t(plural.replace('@count', '@count[' + index + ']'), args, options);
        }
    }
    ;

    /**
 * Returns the passed in URL as an absolute URL.
 *
 * @param url
 *   The URL string to be normalized to an absolute URL.
 *
 * @return
 *   The normalized, absolute URL.
 *
 * @see https://github.com/angular/angular.js/blob/v1.4.4/src/ng/urlUtils.js
 * @see https://grack.com/blog/2009/11/17/absolutizing-url-in-javascript
 * @see https://github.com/jquery/jquery-ui/blob/1.11.4/ui/tabs.js#L53
 */
    Drupal.absoluteUrl = function(url) {
        var urlParsingNode = document.createElement('a');

        // Decode the URL first; this is required by IE <= 6. Decoding non-UTF-8
        // strings may throw an exception.
        try {
            url = decodeURIComponent(url);
        } catch (e) {}

        urlParsingNode.setAttribute('href', url);

        // IE <= 7 normalizes the URL when assigned to the anchor node similar to
        // the other browsers.
        return urlParsingNode.cloneNode(false).href;
    }
    ;

    /**
 * Returns true if the URL is within Drupal's base path.
 *
 * @param url
 *   The URL string to be tested.
 *
 * @return
 *   Boolean true if local.
 *
 * @see https://github.com/jquery/jquery-ui/blob/1.11.4/ui/tabs.js#L58
 */
    Drupal.urlIsLocal = function(url) {
        // Always use browser-derived absolute URLs in the comparison, to avoid
        // attempts to break out of the base path using directory traversal.
        var absoluteUrl = Drupal.absoluteUrl(url);
        var protocol = location.protocol;

        // Consider URLs that match this site's base URL but use HTTPS instead of HTTP
        // as local as well.
        if (protocol === 'http:' && absoluteUrl.indexOf('https:') === 0) {
            protocol = 'https:';
        }
        var baseUrl = protocol + '//' + location.host + Drupal.settings.basePath.slice(0, -1);

        // Decoding non-UTF-8 strings may throw an exception.
        try {
            absoluteUrl = decodeURIComponent(absoluteUrl);
        } catch (e) {}
        try {
            baseUrl = decodeURIComponent(baseUrl);
        } catch (e) {}

        // The given URL matches the site's base URL, or has a path under the site's
        // base URL.
        return absoluteUrl === baseUrl || absoluteUrl.indexOf(baseUrl + '/') === 0;
    }
    ;

    /**
 * Generate the themed representation of a Drupal object.
 *
 * All requests for themed output must go through this function. It examines
 * the request and routes it to the appropriate theme function. If the current
 * theme does not provide an override function, the generic theme function is
 * called.
 *
 * For example, to retrieve the HTML for text that should be emphasized and
 * displayed as a placeholder inside a sentence, call
 * Drupal.theme('placeholder', text).
 *
 * @param func
 *   The name of the theme function to call.
 * @param ...
 *   Additional arguments to pass along to the theme function.
 * @return
 *   Any data the theme function returns. This could be a plain HTML string,
 *   but also a complex object.
 */
    Drupal.theme = function(func) {
        var args = Array.prototype.slice.apply(arguments, [1]);

        return (Drupal.theme[func] || Drupal.theme.prototype[func]).apply(this, args);
    }
    ;

    /**
 * Freeze the current body height (as minimum height). Used to prevent
 * unnecessary upwards scrolling when doing DOM manipulations.
 */
    Drupal.freezeHeight = function() {
        Drupal.unfreezeHeight();
        $('<div id="freeze-height"></div>').css({
            position: 'absolute',
            top: '0px',
            left: '0px',
            width: '1px',
            height: $('body').css('height')
        }).appendTo('body');
    }
    ;

    /**
 * Unfreeze the body height.
 */
    Drupal.unfreezeHeight = function() {
        $('#freeze-height').remove();
    }
    ;

    /**
 * Encodes a Drupal path for use in a URL.
 *
 * For aesthetic reasons slashes are not escaped.
 */
    Drupal.encodePath = function(item, uri) {
        uri = uri || location.href;
        return encodeURIComponent(item).replace(/%2F/g, '/');
    }
    ;

    /**
 * Get the text selection in a textarea.
 */
    Drupal.getSelection = function(element) {
        if (typeof element.selectionStart != 'number' && document.selection) {
            // The current selection.
            var range1 = document.selection.createRange();
            var range2 = range1.duplicate();
            // Select all text.
            range2.moveToElementText(element);
            // Now move 'dummy' end point to end point of original range.
            range2.setEndPoint('EndToEnd', range1);
            // Now we can calculate start and end points.
            var start = range2.text.length - range1.text.length;
            var end = start + range1.text.length;
            return {
                'start': start,
                'end': end
            };
        }
        return {
            'start': element.selectionStart,
            'end': element.selectionEnd
        };
    }
    ;

    /**
 * Add a global variable which determines if the window is being unloaded.
 *
 * This is primarily used by Drupal.displayAjaxError().
 */
    Drupal.beforeUnloadCalled = false;
    $(window).bind('beforeunload pagehide', function() {
        Drupal.beforeUnloadCalled = true;
    });

    /**
 * Displays a JavaScript error from an Ajax response when appropriate to do so.
 */
    Drupal.displayAjaxError = function(message) {
        // Skip displaying the message if the user deliberately aborted (for example,
        // by reloading the page or navigating to a different page) while the Ajax
        // request was still ongoing. See, for example, the discussion at
        // http://stackoverflow.com/questions/699941/handle-ajax-error-when-a-user-clicks-refresh.
        if (!Drupal.beforeUnloadCalled) {
            alert(message);
        }
    }
    ;

    /**
 * Build an error message from an Ajax response.
 */
    Drupal.ajaxError = function(xmlhttp, uri, customMessage) {
        var statusCode, statusText, pathText, responseText, readyStateText, message;
        if (xmlhttp.status) {
            statusCode = "\n" + Drupal.t("An AJAX HTTP error occurred.") + "\n" + Drupal.t("HTTP Result Code: !status", {
                '!status': xmlhttp.status
            });
        } else {
            statusCode = "\n" + Drupal.t("An AJAX HTTP request terminated abnormally.");
        }
        statusCode += "\n" + Drupal.t("Debugging information follows.");
        pathText = "\n" + Drupal.t("Path: !uri", {
            '!uri': uri
        });
        statusText = '';
        // In some cases, when statusCode == 0, xmlhttp.statusText may not be defined.
        // Unfortunately, testing for it with typeof, etc, doesn't seem to catch that
        // and the test causes an exception. So we need to catch the exception here.
        try {
            statusText = "\n" + Drupal.t("StatusText: !statusText", {
                '!statusText': $.trim(xmlhttp.statusText)
            });
        } catch (e) {}

        responseText = '';
        // Again, we don't have a way to know for sure whether accessing
        // xmlhttp.responseText is going to throw an exception. So we'll catch it.
        try {
            responseText = "\n" + Drupal.t("ResponseText: !responseText", {
                '!responseText': $.trim(xmlhttp.responseText)
            });
        } catch (e) {}

        // Make the responseText more readable by stripping HTML tags and newlines.
        responseText = responseText.replace(/<("[^"]*"|'[^']*'|[^'">])*>/gi, "");
        responseText = responseText.replace(/[\n]+\s+/g, "\n");

        // We don't need readyState except for status == 0.
        readyStateText = xmlhttp.status == 0 ? ("\n" + Drupal.t("ReadyState: !readyState", {
            '!readyState': xmlhttp.readyState
        })) : "";

        // Additional message beyond what the xmlhttp object provides.
        customMessage = customMessage ? ("\n" + Drupal.t("CustomMessage: !customMessage", {
            '!customMessage': customMessage
        })) : "";

        message = statusCode + pathText + statusText + customMessage + responseText + readyStateText;
        return message;
    }
    ;

    // Class indicating that JS is enabled; used for styling purpose.
    $('html').addClass('js');

    // 'js enabled' cookie.
    document.cookie = 'has_js=1; path=/';

    /**
 * Additions to jQuery.support.
 */
    $(function() {
        /**
   * Boolean indicating whether or not position:fixed is supported.
   */
        if (jQuery.support.positionFixed === undefined) {
            var el = $('<div style="position:fixed; top:10px" />').appendTo(document.body);
            jQuery.support.positionFixed = el[0].offsetTop === 10;
            el.remove();
        }
    });

    //Attach all behaviors.
    $(function() {
        Drupal.attachBehaviors(document, Drupal.settings);
    });

    /**
 * The default themes.
 */
    Drupal.theme.prototype = {

        /**
   * Formats text for emphasized display in a placeholder inside a sentence.
   *
   * @param str
   *   The text to format (plain-text).
   * @return
   *   The formatted text (html).
   */
        placeholder: function(str) {
            return '<em class="placeholder">' + Drupal.checkPlain(str) + '</em>';
        }
    };

}
)(jQuery);
```

## progress.js
```js
(function ($) {

/**
 * A progressbar object. Initialized with the given id. Must be inserted into
 * the DOM afterwards through progressBar.element.
 *
 * method is the function which will perform the HTTP request to get the
 * progress bar state. Either "GET" or "POST".
 *
 * e.g. pb = new progressBar('myProgressBar');
 *      some_element.appendChild(pb.element);
 */
Drupal.progressBar = function (id, updateCallback, method, errorCallback) {
  var pb = this;
  this.id = id;
  this.method = method || 'GET';
  this.updateCallback = updateCallback;
  this.errorCallback = errorCallback;

  // The WAI-ARIA setting aria-live="polite" will announce changes after users
  // have completed their current activity and not interrupt the screen reader.
  this.element = $('<div class="progress" aria-live="polite"></div>').attr('id', id);
  this.element.html('<div class="bar"><div class="filled"></div></div>' +
                    '<div class="percentage"></div>' +
                    '<div class="message">&nbsp;</div>');
};

/**
 * Set the percentage and status message for the progressbar.
 */
Drupal.progressBar.prototype.setProgress = function (percentage, message) {
  if (percentage >= 0 && percentage <= 100) {
    $('div.filled', this.element).css('width', percentage + '%');
    $('div.percentage', this.element).html(percentage + '%');
  }
  $('div.message', this.element).html(message);
  if (this.updateCallback) {
    this.updateCallback(percentage, message, this);
  }
};

/**
 * Start monitoring progress via Ajax.
 */
Drupal.progressBar.prototype.startMonitoring = function (uri, delay) {
  this.delay = delay;
  this.uri = uri;
  this.sendPing();
};

/**
 * Stop monitoring progress via Ajax.
 */
Drupal.progressBar.prototype.stopMonitoring = function () {
  clearTimeout(this.timer);
  // This allows monitoring to be stopped from within the callback.
  this.uri = null;
};

/**
 * Request progress data from server.
 */
Drupal.progressBar.prototype.sendPing = function () {
  if (this.timer) {
    clearTimeout(this.timer);
  }
  if (this.uri) {
    var pb = this;
    // When doing a post request, you need non-null data. Otherwise a
    // HTTP 411 or HTTP 406 (with Apache mod_security) error may result.
    $.ajax({
      type: this.method,
      url: this.uri,
      data: '',
      dataType: 'json',
      success: function (progress) {
        // Display errors.
        if (progress.status == 0) {
          pb.displayError(progress.data);
          return;
        }
        // Update display.
        pb.setProgress(progress.percentage, progress.message);
        // Schedule next timer.
        pb.timer = setTimeout(function () { pb.sendPing(); }, pb.delay);
      },
      error: function (xmlhttp) {
        pb.displayError(Drupal.ajaxError(xmlhttp, pb.uri));
      }
    });
  }
};

/**
 * Display errors on the page.
 */
Drupal.progressBar.prototype.displayError = function (string) {
  var error = $('<div class="messages error"></div>').html(string);
  $(this.element).before(error).hide();

  if (this.errorCallback) {
    this.errorCallback(this);
  }
};

})(jQuery);
```

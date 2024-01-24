-- Table: public.executives

-- DROP TABLE IF EXISTS public.executives;

CREATE TABLE IF NOT EXISTS public.executives
(
    executive_id uuid NOT NULL,
    executive_name text COLLATE pg_catalog."default" NOT NULL,
    executive_title text COLLATE pg_catalog."default" NOT NULL,
    org_name text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT executives_pkey PRIMARY KEY (executive_id),
    CONSTRAINT executives_org_name_fkey FOREIGN KEY (org_name)
        REFERENCES public.organization (org_name) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.executives
    OWNER to root;
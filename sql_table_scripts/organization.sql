-- Table: public.organization

-- DROP TABLE IF EXISTS public.organization;

CREATE TABLE IF NOT EXISTS public.organization
(
    org_id uuid NOT NULL,
    org_name text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT organization_pkey PRIMARY KEY (org_name),
    CONSTRAINT organization_org_name_org_name1_key UNIQUE (org_name)
        INCLUDE(org_name)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.organization
    OWNER to root;